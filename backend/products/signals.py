from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver

from common.upload import compress_image

from .models import Category, Product, ProductVariant


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
        instance.avatar = compress_image(image_field=instance.avatar, quality=90)

    if hasattr(instance, "image") and instance.image:
        instance.image = compress_image(image_field=instance.image, quality=80)


@receiver(post_save, sender=Product)
def generate_product_seo(sender, instance: Product, **kwargs):
    """
    Автоматически заполняет SEO поля для продукта при сохранении
    """
    # Базовый title
    if instance.title:
        instance.title_seo = f"{instance.title} — купить в интернет-магазине одежды"
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

    # OpenGraph
    instance.og_title = instance.title_seo
    instance.og_description = instance.description

    # JSON-LD для продукта
    product_json_ld = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": instance.title or "Товар",
        "image": instance.avatar.url if instance.avatar else None,
        "description": instance.description,
        "sku": instance.sku or "",
        "brand": {
            "@type": "Brand",
            "name": instance.brand.name if instance.brand else "",
        },
        "offers": {
            "@type": "Offer",
            "priceCurrency": "RUB",
            "price": str(instance.price),
            "availability": (
                "https://schema.org/InStock"
                if instance.is_active
                else "https://schema.org/OutOfStock"
            ),
            "url": f"/products/{instance.id}/",  # или slug, если есть
        },
    }

    instance.json_ld = product_json_ld

    # Сохраняем снова, чтобы записать SEO поля
    # Используем update_fields, чтобы избежать рекурсии сигнала
    instance.save(
        update_fields=[
            "title_seo",
            "description",
            "og_title",
            "og_description",
            "json_ld",
        ]
    )
