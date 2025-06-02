from common.mixins import WebpImageMixin
from common.models import BaseDate, BaseDescription, BaseID, BaseName, BaseTitle
from common.validators import validate_image_extension_and_format
from common.upload_to import dynamic_upload_to
import stripe
from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timesince import timesince
from common.types import COLORS_TYPE, CURRENCY_TYPE, GENDER_TYPE, SIZE_TYPE
from common.upload import compress_image
from users.models import User

# stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_key = "sasdadasdasdasdasdasdasd"


def generate_unique_slug(instance, slug_base):
    slug = slugify(slug_base)
    unique_slug = slug
    num = 1

    ModelClass = instance.__class__

    while ModelClass.objects.filter(slug=unique_slug).exclude(pk=instance.pk).exists():
        unique_slug = f"{slug}-{num}"
        num += 1

    return unique_slug


# def get_unique_slug(model, name):
#     base_slug = slugify(name)
#     slug = base_slug
#     counter = 1
#     while model.objects.filter(slug=slug).exists():
#         slug = f"{base_slug}-{counter}"
#         counter += 1
#     return slug


class Category(BaseID, BaseName):
    """
    Товар
    """

    slug = models.SlugField(blank=True, null=True)
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children",
    )

    def save(self, *args, **kwargs):
        if not self.slug or self.slug.strip() == "":
            if self.parent:
                base_slug = f"{self.parent.name}-{self.name}"
            else:
                base_slug = self.name

            self.slug = generate_unique_slug(self, base_slug)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(BaseID, BaseTitle, BaseDescription, BaseDate):
    """
    Продукт
    """

    # class CURRENCY_TYPE(models.TextChoices):
    #     RUB = "RUB", "RUB"
    #     USD = "USD", "USD"
    #     EUR = "EUR", "EUR"

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
        verbose_name="Категория",
    )
    avatar = models.ImageField(
        "Изображение",
        validators=[validate_image_extension_and_format],
        upload_to=dynamic_upload_to,
        null=True,
        blank=True,
    )
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2, default=0)
    currency = models.CharField("Валюта", max_length=3, choices=CURRENCY_TYPE)
    is_active = models.BooleanField("Активен", default=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def save(self, *args, **kwargs):
        if self.avatar:
            self.avatar = compress_image(self.avatar)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProductVariant(models.Model):
    """
    Вариант продукта
    """

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="variants"
    )
    color = models.CharField("Цвет", max_length=50, choices=COLORS_TYPE)
    size = models.CharField("Размер", max_length=10, choices=SIZE_TYPE)
    # gender = models.CharField("Пол", max_length=10, choices=GENDER_TYPE)
    quantity = models.PositiveIntegerField("Количество на складе", default=0)

    class Meta:
        verbose_name = "Вариант товара"
        verbose_name_plural = "Варианты товара"
        unique_together = ("product", "color", "size")


class ProductImage(models.Model, WebpImageMixin):
    """
    Изображение продукта
    """

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(
        "Изображение",
        validators=[validate_image_extension_and_format],
        upload_to=dynamic_upload_to,
    )

    class Meta:
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товара"

    def __str__(self):
        return self.product.title


class ProductReview(BaseID, BaseName, BaseDescription, BaseDate):
    """
    Отзыв продукта
    """

    email = models.EmailField("Email")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="reviews"
    )
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    @property
    def time_age(self):
        return timesince(self.created_timestamp)


class Wishlist(BaseDate):
    """
    Избранное
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlist")
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="wishlisted_by"
    )

    class Meta:
        unique_together = ("user", "product")


class Cart(BaseID, BaseDate):
    """
    Корзина
    """

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cart", verbose_name="Пользователь"
    )

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self):
        return f"Корзина пользователя {self.user}"


class CartItem(BaseID):
    """
    Позиция в корзине
    """

    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="items", verbose_name="Корзина"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")

    class Meta:
        unique_together = ("cart", "product")
        verbose_name = "Позиция в корзине"
        verbose_name_plural = "Позиции в корзине"

    def __str__(self):
        return f"Товар {self.product} в корзине {self.cart}"
