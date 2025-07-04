# Generated by Django 5.1 on 2025-06-13 11:20

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Дата обновления"),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Имя"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Фамилия"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Город"
                    ),
                ),
                (
                    "street",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Улица"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Профиль",
                "verbose_name_plural": "Профили",
            },
        ),
    ]
