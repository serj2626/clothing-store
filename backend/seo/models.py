import os
from io import BytesIO

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.db import models
from PIL import Image

from common.models import BaseSEO


def validate_image_extension(value):
    ext = os.path.splitext(value.name)[1].lower()
    valid_extensions = [".jpg", ".jpeg", ".png", ".webp"]
    if ext not in valid_extensions:
        raise ValidationError(
            f"Недопустимое расширение '{ext}'. Разрешены: jpg, jpeg, png, webp."
        )


class SEO(BaseSEO):
    """
    SEO модель
    """

    class OGType(models.TextChoices):
        """
        Типы Open Graph для SEO вашего сайта по продаже металла
        """

        WEBSITE = (
            "website",
            "Website — общая веб-страница (главная, контакты, о компании)",
        )
        PRODUCT = "product", "Product — товар (металл, металлопродукция)"
        SERVICE = (
            "service",
            "Service — услуга, сервис (резка, доставка, обработка металла)",
        )
        BLOG = "blog", "Blog — блог, новости, статьи"
        ARTICLE = (
            "article",
            "Article — статьи и новости (альтернатива для блога)",
        )
        PROFILE = (
            "profile",
            "Profile — профиль человека (контакты, сотрудники)",
        )
        BOOK = "book", "Book — книга (редко используется, можно удалить)"
        PLACE = "place", "Place — место (например, филиалы компании)"
        ACTIVITY = (
            "activity",
            "Activity — действие пользователя (логирование действий, редко используется)",
        )

    slug = models.CharField(
        "URL путь",
        max_length=255,
        unique=True,
        help_text="URL путь, например: about/ (без начального и конечного слэша)",
    )
    canonical_url = models.URLField(
        "Canonical URL",
        blank=True,
        null=True,
        help_text="Полный URL для canonical ссылки",
    )
    noindex = models.BooleanField(
        "Noindex", default=False, help_text="Запретить индексацию страницы"
    )
    nofollow = models.BooleanField(
        "Nofollow",
        default=False,
        help_text="Запретить переход по ссылкам на странице",
    )

    og_image = models.ImageField(
        "OG Изображение",
        upload_to="seo/",
        blank=True,
        null=True,
        validators=[validate_image_extension],
    )
    og_type = models.CharField(
        "OG Тип",
        max_length=50,
        choices=OGType.choices,
        default=OGType.WEBSITE,
        help_text="Тип Open Graph: website, article, product...",
    )
    og_site_name = models.CharField(
        "OG Site Name",
        max_length=255,
        blank=True,
        null=True,
        help_text="Название сайта для Open Graph",
    )
    lastmod = models.DateTimeField("Дата последнего изменения", auto_now=True)

    def save(self, *args, **kwargs):
        # Сжимаем og_image, если оно есть и изменено
        if self.og_image and hasattr(self.og_image, "file"):
            img = Image.open(self.og_image)
            img = img.convert("RGB")  # для webp/png совместимости
            output = BytesIO()
            img.save(output, format="JPEG", quality=75, optimize=True)
            output.seek(0)
            self.og_image = ContentFile(output.read(), self.og_image.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"SEO: {self.slug}"

    class Meta:
        verbose_name = "SEO"
        verbose_name_plural = "SEO"
        ordering = ["slug"]


class RobotsTXT(models.Model):
    """
    Управление текстом robots.txt через админку.
    """

    text = models.TextField(
        verbose_name="Текст файла robots.txt",
        default=""" User-agent: *
                    Disallow: /admin/
                    Disallow: /api/
                    Sitemap: https://yourdomain.com/sitemap.xml
                    """,
        help_text="Текст файла robots.txt, который будет отдавать сервер.",
    )

    class Meta:
        verbose_name = "robots.txt"
        verbose_name_plural = "robots.txt"

    def __str__(self):
        return "robots.txt"


class Webmaster(models.Model):
    TYPE_YANDEX = "yandex"
    TYPE_GOOGLE = "google"

    TYPES = (
        (TYPE_YANDEX, "Яндекс.Вебмастер"),
        (TYPE_GOOGLE, "Google Search Console"),
    )

    type = models.CharField(
        max_length=50,
        choices=TYPES,
        default=TYPES,
        verbose_name="Вебмастер",
        unique=True,
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Наименование файла без расширения",
        help_text="Для Яндекса текст файла будет совпадать с наименованием файла",
    )
    text = models.TextField(max_length=1000, verbose_name="Текст файла")

    class Meta:
        verbose_name = "Верификация для вебмастера"
        verbose_name_plural = "Верификация вебмастеров"

    def __str__(self):
        return f"Файл {self.get_type_display()}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        with open(
            os.path.join(settings.BASE_DIR, f"{self.title}.html"),
            "w+",
            encoding="utf-8",
        ) as file:
            file.write(self.text)
