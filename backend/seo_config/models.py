from django.db import models
import os
from django.utils import timezone
from django.core.exceptions import ValidationError
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile
from django.contrib.sitemaps import Sitemap
from django.core.validators import MinValueValidator, MaxValueValidator

# from .models import Article


def validate_image_extension(value):
    ext = os.path.splitext(value.name)[1].lower()
    valid_extensions = [".jpg", ".jpeg", ".png", ".webp"]
    if ext not in valid_extensions:
        raise ValidationError(
            f"Недопустимое расширение '{ext}'. Разрешены: jpg, jpeg, png, webp."
        )


class SEO(models.Model):
    """
    SEO модель
    """

    class ChangeFrequency(models.TextChoices):
        """
        Перечисление частоты обновления сайта
        """

        ALWAYS = "always", "Всегда"
        HOURLY = "hourly", "Каждый час"
        DAILY = "daily", "Ежедневно"
        WEEKLY = "weekly", "Еженедельно"
        MONTHLY = "monthly", "Ежемесячно"
        YEARLY = "yearly", "Ежегодно"
        NEVER = "never", "Никогда"

    slug = models.SlugField(
        "URL путь",
        max_length=255,
        unique=True,
        help_text="URL путь, например: about/ (без начального и конечного слэша)",
    )
    title = models.CharField(
        "Заголовок (title)", max_length=255, blank=True, help_text="Макс. 60 символов"
    )
    description = models.TextField(
        "Описание (meta description)", blank=True, help_text="Макс. 160 символов"
    )
    keywords = models.CharField(
        "Ключевые слова (meta keywords)",
        max_length=255,
        blank=True,
        help_text="Через запятую",
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
        "Nofollow", default=False, help_text="Запретить переход по ссылкам на странице"
    )

    og_title = models.CharField("OG Заголовок", max_length=255, blank=True)
    og_description = models.TextField("OG Описание", blank=True)
    og_image = models.ImageField(
        "OG Изображение",
        upload_to="seo/",
        blank=True,
        null=True,
        validators=[validate_image_extension],
    )

    # Для sitemap
    priority = models.DecimalField(
        "Приоритет в sitemap",
        max_digits=2,
        decimal_places=1,
        default=0.5,
        help_text="От 0.1 до 1.0",
    )
    changefreq = models.CharField(
        "Частота изменений",
        max_length=10,
        choices=ChangeFrequency.choices,
        default=ChangeFrequency.WEEKLY,
    )
    lastmod = models.DateTimeField("Дата последнего изменения", auto_now=True)

    # JSON-LD / Schema.org
    json_ld = models.TextField(
        "JSON-LD разметка",
        blank=True,
        help_text="Дополнительная структурированная разметка",
    )

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


class RobotsTxt(models.Model):
    content = models.TextField("Содержимое robots.txt")
    is_active = models.BooleanField("Активен", default=True)

    class Meta:
        verbose_name = "robots.txt"
        verbose_name_plural = "robots.txt"

    def __str__(self):
        return "robots.txt (активный)" if self.is_active else "robots.txt (неактивный)"


class SitemapItem(models.Model):
    """
    Модель для элементов карты сайта
    """

    loc = models.URLField("URL страницы", max_length=2048)
    lastmod = models.DateTimeField("Дата последнего изменения", default=timezone.now)
    changefreq = models.CharField(
        "Частота изменений",
        max_length=10,
        choices=SEO.ChangeFrequency.choices,
        default=SEO.ChangeFrequency.WEEKLY,
    )
    priority = models.DecimalField(
        "Приоритет",
        max_digits=2,
        decimal_places=1,
        default=0.5,
        validators=[MinValueValidator(0.1), MaxValueValidator(1.0)],
    )
    is_active = models.BooleanField("Активен", default=True)

    class Meta:
        verbose_name = "Элемент карты сайта"
        verbose_name_plural = "Элементы карты сайта"
        ordering = ["-priority"]

    def __str__(self):
        return f"Sitemap: {self.loc}"


# class ArticleSitemap(Sitemap):
#     changefreq = "weekly"
#     priority = 0.8

#     def items(self):
#         return Article.objects.filter(published=True)

#     def lastmod(self, obj):
#         return obj.updated_at
