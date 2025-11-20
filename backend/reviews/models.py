from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.timesince import timesince

from common.mixins import WebpImageMixin
from common.models import BaseDate, BaseDescription, BaseID
from common.upload_to import dynamic_upload_to
from common.validators import validate_image_extension_and_format
from products.models import Product
from users.models import User


class Review(BaseID, BaseDescription, BaseDate):
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
    name = models.CharField("Имя", max_length=100, null=True, blank=True)
    email = models.EmailField("Email")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="reviews"
    )
    advantages = models.TextField("Достоинства", blank=True, null=True)
    disadvantages = models.TextField("Недостатки", blank=True, null=True)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    is_published = models.BooleanField("Опубликован", default=False)
    likes = models.ManyToManyField(User, related_name="+", blank=True)
    dislikes = models.ManyToManyField(User, related_name="+", blank=True)

    @property
    def time_age(self):
        return timesince(self.created_at) + " назад"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["-created_at"]
        unique_together = ["user", "product"]

    def __str__(self):
        return f"Отзыв от {self.name}"


class ReviewCompanyReply(BaseID, BaseDescription, BaseDate):
    """
    Ответ компании на отзыв продукта
    Только пользователи с правами администратора (компания) могут создавать ответы
    """

    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="replies")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"is_staff": True},
        verbose_name="Автор (компания)",
    )

    def save(self, *args, **kwargs):
        if not self.author.is_staff:
            raise PermissionError("Только сотрудники компании могут отвечать на отзывы")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Ответ компании"
        verbose_name_plural = "Ответы компании"
        permissions = [
            ("can_reply_to_reviews", "Может отвечать на отзывы"),
        ]

    @property
    def time_age(self):
        return timesince(self.created_timestamp)


class ReviewPhoto(BaseDate, WebpImageMixin):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name="photos",
        verbose_name="Отзыв",
    )
    image = models.ImageField(
        "Фотография",
        upload_to=dynamic_upload_to,
        validators=[validate_image_extension_and_format],
    )
    alt = models.CharField(
        "Описание", max_length=100, default="Описание", blank=True, null=True
    )

    class Meta:
        verbose_name = "Фотография отзыва"
        verbose_name_plural = "Фотографии отзывов"

    def __str__(self):
        return f"Фото для отзыва #{self.review.id}"
