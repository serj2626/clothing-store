import stripe
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey
from transliterate import slugify as ru_slugify

from common.mixins import CommentableMixin, LikeableMixin, WebpImageMixin
from common.models import (
    BaseContent,
    BaseDate,
    BaseDescription,
    BaseID,
    BaseName,
    BaseSEO,
    BaseTitle,
)
from common.types import COUNTRY_TYPE, GENDER_TYPE
from common.upload import compress_image
from common.upload_to import dynamic_upload_to
from users.models import User

from .utils.validators import validate_file_size, validate_image_size

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
        'Изображение',
        upload_to=dynamic_upload_to,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "webp"]),
            validate_image_size,
            validate_file_size,
        ],
        null=True,
        blank=True,
    )
    slug = models.SlugField("URL", max_length=100, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ru_slugify(self.name)
        if self.image:
            self.image = compress_image(self.image)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.get_country_display()}"


class Category(MPTTModel, BaseID, BaseName, WebpImageMixin):
    """
    Категория товаров
    """

    slug = models.SlugField("слаг", max_length=100, blank=True, null=True)
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
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "webp"]),
            validate_image_size,
            validate_file_size,
        ],
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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ru_slugify(self.name)
        if self.image:
            self.image = compress_image(self.image)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})


class ProductSize(BaseTitle):
    """
    Размер продукта
    """

    slug = models.SlugField("слаг", max_length=100, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ru_slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Размер продукта"
        verbose_name_plural = "Размеры продуктов"
        unique_together = ("title",)

    def __str__(self):
        return self.title


class ProductColor(BaseTitle):
    """
    Цвет продукта
    """

    color = models.CharField(
        "Цвет",
        max_length=100,
        default="#000000",
        unique=True,
        help_text='цвета бери тут: https://htmlcolors.com/google-color-picker',
    )

    slug = models.SlugField("слаг", max_length=100, unique=True, blank=True, null=True)

    def clean(self):
        if not (
            self.color.startswith("#")
            or self.color.startswith("rgb")
            or self.color.startswith("rgba")
        ):
            raise ValidationError("Цвет должен начинаться с # или с rgb/rgba")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ru_slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Цвет продукта"
        verbose_name_plural = "Цвета продуктов"
        unique_together = ("title",)

    def __str__(self):
        return self.title


class Product(
    BaseID,
    BaseTitle,
    BaseDate,
    BaseContent,
    LikeableMixin,
    CommentableMixin,
    BaseSEO,
):
    """
    Продукт
    """

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
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2, default=0)
    gender = models.CharField("Пол", max_length=6, choices=GENDER_TYPE, default="M")
    is_active = models.BooleanField("Активен", default=True)
    sku = models.CharField(
        "артикул", max_length=100, null=True, blank=True, unique=True
    )
    avatar = models.ImageField(
        upload_to=dynamic_upload_to,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "webp"]),
            validate_file_size,
        ],
        null=True,
        blank=True,
    )

    @property
    def count(self):
        return self.__class__.objects.count()

    def generate_sku(self):
        brand_code = (self.brand.name[:2] if self.brand else "NON").upper()
        cat_code = (
            ru_slugify(self.category.name[:2]) if self.category else "GEN"
        ).upper()
        gender_code = (self.gender if self.gender else "U").upper()
        id_code = f"{str(self.id)[-4:].upper()}{self.count}"
        return f"{brand_code}-{cat_code}-{gender_code}-{id_code}"

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.title


class ProductVariant(models.Model):
    """
    Вариант продукта
    """

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="variants"
    )
    color = models.ForeignKey(
        ProductColor,
        on_delete=models.PROTECT,
        verbose_name="Цвет",
    )
    size = models.ForeignKey(
        ProductSize,
        on_delete=models.PROTECT,
        verbose_name="Размер",
    )
    quantity = models.PositiveIntegerField("Количество на складе", default=0)
    image = models.ImageField(
        upload_to=dynamic_upload_to,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "webp"]),
            validate_file_size,
        ],
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Вариант товара"
        verbose_name_plural = "Варианты товара"
        unique_together = ("product", "color", "size")


class Favorite(BaseDate):
    """
    Избранное
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    product = models.ForeignKey(
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
        "Product",
        blank=True,
        related_name="discounts",
        verbose_name="Продукты",
    )
    categories = models.ManyToManyField(
        "Category",
        blank=True,
        related_name="discounts",
        verbose_name="Категории",
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
