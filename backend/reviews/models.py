from django.core.exceptions import ValidationError
from django.core.validators import (
    FileExtensionValidator,
    MaxValueValidator,
    MinValueValidator,
)
from django.db import models

from common.mixins import WebpImageMixin
from common.models import BaseDate, BaseReview
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
    likes = models.ManyToManyField(
        User, related_name="+", blank=True, verbose_name="Лайки"
    )
    dislikes = models.ManyToManyField(
        User, related_name="+", blank=True, verbose_name="Дизлайки"
    )

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["-created_at"]
        unique_together = ["user", "product"]

    def get_count_likes(self):
        return self.likes.count()
    
    get_count_likes.short_description = "Количество лайков"

    def get_count_dislikes(self):
        return self.dislikes.count()
    
    get_count_dislikes.short_description = "Количество дизлайков"
    
    def __str__(self):
        return f"Отзыв от {self.user.email} на {self.product.title}"


class ReviewCompanyReply(BaseReview):
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


class ReviewPhoto(BaseDate, WebpImageMixin):
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
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Фотография отзыва"
        verbose_name_plural = "Фотографии отзывов"

    def __str__(self):
        return f"Фото для отзыва #{self.review.id}"
