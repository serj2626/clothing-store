from common.mixins import AvatarPreviewMixin, WebpImageMixin
from common.models import BaseDate, BaseDescription, BaseID, BaseName, BaseTitle
from common.validators import validate_image_extension_and_format
from common.upload_to import dynamic_upload_to
import stripe
from django.urls import reverse
from common.utils import get_client_ip
from mptt.models import MPTTModel, TreeForeignKey
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timesince import timesince
from common.types import (
    COLORS_TYPE,
    COUNTRY_TYPE,
    CURRENCY_TYPE,
    GENDER_TYPE,
    SIZE_TYPE,
)
from django.utils.html import format_html
from common.upload import compress_image
from users.models import User
from django.utils import timezone

# stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_key = "sasdadasdasdasdasdasdasd"


class Brand(BaseID, BaseName, BaseDescription, WebpImageMixin):
    """
    Бренд
    """

    country = models.CharField(
        "Страна",
        max_length=100,
        choices=COUNTRY_TYPE,
        default="cn",
        null=True,
        blank=True,
    )
    image = models.ImageField(
        "Изображение",
        validators=[validate_image_extension_and_format],
        upload_to=dynamic_upload_to,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"

    def __str__(self):
        return f"{self.name} - {self.get_country_display()}"


class Category(MPTTModel, BaseID, BaseName, WebpImageMixin):
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
    image = models.ImageField(
        "Изображение",
        validators=[validate_image_extension_and_format],
        upload_to=dynamic_upload_to,
        null=True,
        blank=True,
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
        return reverse("category_detail", kwargs={"slug": self.slug})


class Product(BaseID, BaseTitle, BaseDate, WebpImageMixin, AvatarPreviewMixin):
    """
    Продукт
    """

    image_field_name = "avatar"

    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
        verbose_name="Бренд",
    )
    category = TreeForeignKey(
        Category,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="products",
        verbose_name="Категория",
    )
    gender = models.CharField("Пол", max_length=6, choices=GENDER_TYPE, default="male")
    avatar = models.ImageField(
        "Изображение",
        validators=[validate_image_extension_and_format],
        upload_to=dynamic_upload_to,
        null=True,
        blank=True,
    )
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2, default=0)
    currency = models.CharField(
        "Валюта", max_length=3, choices=CURRENCY_TYPE, default="RUB"
    )
    is_active = models.BooleanField("Активен", default=True)

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.title


class ProductDetail(BaseTitle, BaseDescription):
    """
    Детали продукта
    """

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="details"
    )

    class Meta:
        verbose_name = "Детали"
        verbose_name_plural = "Детали"


class ProductLike(models.Model):
    """
    Лайк товара
    """

    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="likes", verbose_name="Товар"
    )
    ip_address = models.GenericIPAddressField("IP", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        unique_together = ("product", "ip_address")  # один лайк с одного IP
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"

    def __str__(self):
        return f"{self.ip_address} -> {self.product.title}"


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


class ProductImage(models.Model, WebpImageMixin, AvatarPreviewMixin):
    """
    Изображение продукта
    """

    image_field_name = "image"

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(
        "Изображение",
        validators=[validate_image_extension_and_format],
        upload_to=dynamic_upload_to,
    )
    alt = models.CharField(
        "Описание", max_length=100, default="Описание", blank=True, null=True
    )

    class Meta:
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товара"

    def __str__(self):
        return self.product.title


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

    # @property
    # def has_admin_reply(self):
    #     return hasattr(self, "admin_reply")

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

class ReviewPhoto(BaseDate, WebpImageMixin):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name="photos", verbose_name="Отзыв"
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


class CompanyReply(BaseID, BaseDescription, BaseDate):
    """
    Ответ компании на отзыв продукта
    Только пользователи с правами администратора (компания) могут создавать ответы
    """

    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="replies")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={
            "is_staff": True
        },  # Ограничиваем авторов только staff-пользователями
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


class Favorite(BaseDate):
    """
    Избранное
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="Favoriteed_by"
    )
    variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Выбранный вариант",
    )

    class Meta:
        # unique_together = ("user", "product")
        unique_together = ("user",)
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные"


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
    categories = models.ManyToManyField(
        "Category", blank=True, related_name="discounts", verbose_name="Категории"
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

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="cart"
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
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Товар",
        related_name="products",
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")

    class Meta:
        verbose_name = "Позиция в корзине"
        verbose_name_plural = "Позиции в корзине"

    def __str__(self):
        return f"Товар {self.product} в корзине {self.cart}"

    @classmethod
    def add_or_update(cls, cart, product, quantity=1):
        """
        Добавляет товар в корзину или обновляет количество, если товар уже есть.
        """

        item, created = cls.objects.get_or_create(
            cart=cart, product=product, defaults={"quantity": quantity}
        )
        if not created:
            item.quantity += quantity
            item.save()
        return item
