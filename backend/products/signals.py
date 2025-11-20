from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from common.upload import compress_image
from .models import Product, ProductVariant


@receiver(post_save, sender=Product)
def generate_product_sku(sender, instance, created, **kwargs):
    if created and not instance.sku:
        instance.sku = instance.generate_sku()
        instance.save(update_fields=["sku"])


@receiver(pre_save, sender=Product)
@receiver(pre_save, sender=ProductVariant)
def compress_image_before_save(sender, instance, **kwargs):

    if hasattr(instance, "avatar") and instance.avatar:
        instance.avatar = compress_image(instance.avatar)

    if hasattr(instance, "image") and instance.image:
        instance.image = compress_image(instance.image)
