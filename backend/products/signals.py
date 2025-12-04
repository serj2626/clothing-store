from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .utils.service import generate_json_ld_by_pruduct
from common.upload import compress_image

from .models import Category, CategoryCharacteristic, Product, ProductVariant


@receiver(post_save, sender=ProductVariant)
def add_characteristics_in_category(sender, instance, created, **kwargs):
    product = instance.product
    category = product.category

    if not category:
        return

    CategoryCharacteristic.objects.get_or_create(
        category=category,
        color=instance.color,
        size=instance.size,
    )


# @receiver(post_save, sender=ProductVariant)
# def update_category_characteristics(sender, instance, created, **kwargs):
#     product = instance.product
#     category = product.category

#     if not category:
#         return

#     if created:
#         CategoryCharacteristic.objects.get_or_create(
#             category=category,
#             color=instance.color,
#             size=instance.size
#         )
#     else:
#         # Если цвет или размер обновились – актуализируем характеристики
#         old = sender.objects.get(pk=instance.pk)

#         if old.color != instance.color or old.size != instance.size:
#             # Добавляем новую
#             CategoryCharacteristic.objects.get_or_create(
#                 category=category,
#                 color=instance.color,
#                 size=instance.size
#             )


@receiver(post_save, sender=Product)
def generate_product_sku(sender, instance, created, **kwargs):
    if created and not instance.sku:
        instance.sku = instance.generate_sku()
        instance.save(update_fields=["sku"])


@receiver(pre_save, sender=Product)
@receiver(pre_save, sender=Category)
def normalize_product_title(sender, instance, **kwargs):
    if hasattr(instance, "title"):
        instance.title = instance.title.title().strip()
    if hasattr(instance, 'name'):
        instance.name = instance.name.title().strip()


@receiver(pre_save, sender=Product)
@receiver(pre_save, sender=ProductVariant)
def compress_image_before_save(sender, instance, **kwargs):

    if hasattr(instance, "avatar") and instance.avatar:
        instance.avatar = compress_image(
            image_field=instance.avatar, quality=90
        )

    if hasattr(instance, "image") and instance.image:
        instance.image = compress_image(image_field=instance.image, quality=80)


@receiver(post_save, sender=Product)
def generate_product_seo(sender, instance: Product, **kwargs):
    """
    Автоматически заполняет SEO поля для продукта при сохранении
    """
    if instance.title:
        instance.title_seo = (
            f"{instance.title} — купить в интернет-магазине одежды"
        )
    else:
        instance.title_seo = "Товар — интернет-магазин одежды"

    # Meta description
    parts = []
    if instance.brand:
        parts.append(f"Бренд {instance.brand.name}")
    if instance.category:
        parts.append(f"Категория: {instance.category.title}")
    if instance.price:
        parts.append(f"Цена: {instance.price} руб.")
    parts.append(
        "Доставка по Санкт-Петербургу и России. Гарантия качества и удобные условия оплаты."
    )

    instance.description = " | ".join(parts)
    instance.og_title = instance.title_seo
    instance.og_description = instance.description
    instance.json_ld = generate_json_ld_by_pruduct(instance)

    instance.save(
        update_fields=[
            "title_seo",
            "description",
            "og_title",
            "og_description",
            "json_ld",
        ]
    )
