import uuid

from django.db import models
from django.utils.timesince import timesince
from django_ckeditor_5.fields import CKEditor5Field


class BaseSEO(models.Model):
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

    description = models.TextField(
        "Описание (meta description)",
        blank=True,
    )
    keywords = models.TextField(
        "Ключевые слова (meta keywords)",
        blank=True,
        null=True,
        help_text="Через запятую",
    )
    title_seo = models.CharField(
        "Заголовок (title)",
        max_length=255,
        blank=True,
        help_text="Макс. 255 символов",
    )
    og_title = models.CharField("OG Заголовок", max_length=255, blank=True)
    og_description = models.TextField("OG Описание", blank=True)
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
    json_ld = models.JSONField(
        blank=True, null=True, help_text="JSON-LD schema.org data"
    )

    class Meta:
        abstract = True


class BaseID(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class BaseContent(models.Model):
    content = CKEditor5Field(
        blank=True, verbose_name="Описание", config_name="extends"
    )

    class Meta:
        abstract = True


class BaseTitle(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")

    class Meta:
        abstract = True


class BaseName(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")

    class Meta:
        abstract = True


class BaseDescription(models.Model):
    description = models.TextField(
        verbose_name="Описание", null=True, blank=True
    )

    class Meta:
        abstract = True


class BaseDate(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления"
    )

    class Meta:
        abstract = True


class BaseReview(BaseDescription, BaseDate, models.Model):
    is_published = models.BooleanField("Опубликован", default=False)

    @property
    def time_age(self):
        return timesince(self.created_at) + " назад"

    class Meta:
        abstract = True
