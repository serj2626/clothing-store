from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.utils.timesince import timesince
from common.models import BaseDate


class Notification(BaseDate):
    NOTIFICATION_TYPES = (
        ("order_created", "Товар купили"),
        ("comment_publish", "Ваш комментарий опубликован"),
        ("comment_unpublish", "Ваш комментарий не опубликован"),
        ("comment_reply", "Ответ на комментарий"),
        ("order_status", "Изменение статуса заказа"),
        ("promo", "Персональное предложение"),
        ("system", "Системное уведомление"),
    )

    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications",
        verbose_name="Получатель",
    )
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Отправитель",
    )
    notification_type = models.CharField(
        max_length=20, choices=NOTIFICATION_TYPES, verbose_name="Тип уведомления"
    )
    message = models.TextField(verbose_name="Сообщение")
    is_read = models.BooleanField(default=False, verbose_name="Прочитано")

    # Для связи с разными объектами (заказ, комментарий и т.д.)
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, null=True, blank=True
    )
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey("content_type", "object_id")

    @property
    def time_ago(self):
        return timesince(self.created_at)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомления"

    def __str__(self):
        return f"{self.get_notification_type_display()} для {self.recipient}"
