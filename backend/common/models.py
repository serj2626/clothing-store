import uuid

from django.db import models
from django.utils.timesince import timesince
from django_ckeditor_5.fields import CKEditor5Field


class BaseID(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class BaseContent(models.Model):
    content = CKEditor5Field(blank=True, verbose_name="Описание", config_name="extends")

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
    description = models.TextField(verbose_name="Описание", null=True, blank=True)

    class Meta:
        abstract = True


class BaseDate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        abstract = True


class BaseReview(BaseDescription, BaseDate, models.Model):
    is_published = models.BooleanField("Опубликован", default=False)

    @property
    def time_age(self):
        return timesince(self.created_at) + " назад"

    class Meta:
        abstract = True
