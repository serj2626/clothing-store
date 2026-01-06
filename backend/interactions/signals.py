from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Comment, Review


@receiver(post_save, sender=Review)
def update_product_rating(sender, instance, created, **kwargs):
    if created:
        Comment.objects.create(
            user=instance.user,
            text=instance.description,
            content_object=instance,
            parent=None,
        )
