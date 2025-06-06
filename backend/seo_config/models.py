from django.db import models
import os
from django.core.exceptions import ValidationError
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile
from django.contrib.sitemaps import Sitemap
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

    slug = models.SlugField(
        "Слаг", unique=True, help_text="URL путь, например: /about/"
    )
    title = models.CharField("Заголовок", max_length=255, blank=True)
    description = models.TextField("Описание", blank=True)
    keywords = models.CharField("Ключевые слова", max_length=255, blank=True)

    og_title = models.CharField("OG Заголовок", max_length=255, blank=True)
    og_description = models.TextField("OG Описание", blank=True)
    og_image = models.ImageField(
        "OG Изображение",
        upload_to="seo/",
        blank=True,
        null=True,
        validators=[validate_image_extension],
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


# class ArticleSitemap(Sitemap):
#     changefreq = "weekly"
#     priority = 0.8

#     def items(self):
#         return Article.objects.filter(published=True)

#     def lastmod(self, obj):
#         return obj.updated_at
