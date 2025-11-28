from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.core.validators import (
    FileExtensionValidator,
    MaxValueValidator,
    MinValueValidator,
)
from django.db import models
from django.utils.timesince import timesince

from common.models import BaseDate, BaseReview
from common.upload import compress_image
from common.upload_to import dynamic_upload_to
from products.models import Product
from products.utils.validators import validate_file_size, validate_image_size
from users.models import User


class Review(BaseReview):
    """
    Отзыв продукта
    """

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviews",
        verbose_name="Пользователь",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Товар",
    )
    advantages = models.TextField("Достоинства", blank=True, null=True)
    disadvantages = models.TextField("Недостатки", blank=True, null=True)
    rating = models.PositiveIntegerField(
        'Рейтинг', validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    likes = GenericRelation("Like", related_query_name="review")
    comments = GenericRelation("Comment", related_query_name="review")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["-created_at"]
        unique_together = ["user", "product"]

    def __str__(self):
        return f"Отзыв от {self.user.email} на {self.product.title}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    # древовидность (коммент на коммент)
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="replies",
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    likes = GenericRelation("Like", related_query_name="comment")

    def __str__(self):
        return f"Комментарий от {self.user}"


class ReviewPhoto(BaseDate):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name="photos",
        verbose_name="Отзыв",
    )
    image = models.ImageField(
        "Фотография",
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "webp"]),
            validate_image_size,
            validate_file_size,
        ],
        upload_to=dynamic_upload_to,
    )
    alt = models.CharField(
        "Описание", max_length=100, default="Описание", blank=True, null=True
    )

    def save(self, *args, **kwargs):
        current_review = self.review
        count_photos = ReviewPhoto.objects.filter(review=current_review).count()
        if count_photos >= 5:
            raise ValidationError("Достигнут максимум 5 фотографий")
        self.image = compress_image(self.image)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Фотография отзыва"
        verbose_name_plural = "Фотографии отзывов"

    def __str__(self):
        return f"Фото для отзыва #{self.review.id}"


class Notification(BaseDate):
    NOTIFICATION_TYPES = (
        ("order_created", "Ваш заказ создан"),
        ("comment_publish", "Ваш комментарий опубликован"),
        ("comment_unpublish", "Ваш комментарий не опубликован"),
        ("comment_reply", "Ответ на ваш комментарий"),
        ("order_status", "Изменение статуса заказа"),
        ("promo", "Персональное предложение"),
        ("system", "Системное уведомление"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def time_ago(self):
        return timesince(self.created_at)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомления"

    def __str__(self):
        return f"Уведомление для {self.user}"


class Like(models.Model):
    """
    Лайк
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="likes",
        verbose_name="Пользователь",
    )

    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, verbose_name="Тип контента"
    )
    object_id = models.PositiveIntegerField('ID контента')
    content_object = GenericForeignKey("content_type", "object_id")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "content_type", "object_id")

    def __str__(self):
        return f"Лайк от {self.user} -> {self.content_object}"
