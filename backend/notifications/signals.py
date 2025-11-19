from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Notification


def create_notification(
    recipient, sender, notification_type, message, content_object=None
):
    Notification.objects.create(
        recipient=recipient,
        sender=sender,
        notification_type=notification_type,
        message=message,
        content_object=content_object,
    )


# Пример обработчика для ответов на комментарии
@receiver(post_save, sender="products.CompanyReply")
def handle_comment_reply(sender, instance, created, **kwargs):
    if created:
        create_notification(
            recipient=instance.review.user,
            sender=instance.author,
            notification_type="comment_reply",
            message=f"Магазин ответил на ваш комментарий к товару {instance.review.product.title}",
            content_object=instance,
        )
