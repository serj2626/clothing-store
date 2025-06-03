from common.mixins import WebpImageMixin
from common.models import BaseDate, BaseDescription, BaseID, BaseName, BaseTitle
from common.validators import validate_image_extension_and_format
from common.upload_to import dynamic_upload_to
import stripe
from mptt.models import MPTTModel, TreeForeignKey
from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timesince import timesince
from common.types import COLORS_TYPE, CURRENCY_TYPE, GENDER_TYPE, SIZE_TYPE
from common.upload import compress_image
from users.models import User
from django.utils import timezone

# stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_key = "sasdadasdasdasdasdasdasd"


class Category(MPTTModel, BaseID, BaseName):
    """
    Категория товаров
    """

    slug = models.SlugField("URL", max_length=100, unique=True, blank=True, null=True)
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
        verbose_name="Родительская категория",
    )
    is_active = models.BooleanField("Активна", default=True)

    class MPTTMeta:
        order_insertion_by = ["name"]  # только это поле здесь

    class Meta:
        unique_together = ["slug", "parent"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("products:category", kwargs={"slug": self.slug})


class Product(BaseID, BaseTitle, BaseDescription, BaseDate):
    """
    Продукт
    """

    category = TreeForeignKey(
        Category,
        on_delete=models.PROTECT,
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


class Discount(models.Model):
    """
    Скидка
    """

    amount = models.DecimalField("Скидка в %", max_digits=5, decimal_places=2)
    start_date = models.DateTimeField("Начало действия", default=timezone.now)
    end_date = models.DateTimeField("Окончание действия", null=True, blank=True)
    is_active = models.BooleanField("Активна", default=True)
    products = models.ManyToManyField(
        "Product", blank=True, related_name="discounts", verbose_name="Продукты"
    )

    class Meta:
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"

    def __str__(self):
        return f"{self.name} ({self.amount}%)"

    def is_valid(self):
        now = timezone.now()
        return (
            self.is_active
            and self.start_date <= now
            and (self.end_date is None or now <= self.end_date)
        )


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
