from django.db import models

from common.models import BaseDate
from common.types import CONTACTS_TYPE


class Contact(models.Model):
    """
    Модель контактов
    """

    type = models.CharField(
        max_length=50,
        choices=CONTACTS_TYPE,
        default="phone",
        verbose_name="Тип",
    )
    value = models.TextField(max_length=500, verbose_name="Значение")

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"Контакт {self.get_type_display()}"


class Subscription(BaseDate):
    """
    Подписка на рассылку
    """

    email = models.EmailField("Почта", max_length=255, unique=True)
    verified = models.BooleanField("Проверен", default=False)

    class Meta:
        verbose_name = "Подписка на рассылку"
        verbose_name_plural = "Подписки на рассылку"

    def __str__(self):
        return f"Подписка на рассылку от {self.email} от {self.created_at}"


class Feedback(BaseDate):
    """
    Обратная связь
    """

    name = models.CharField("Имя", max_length=255)
    phone = models.CharField("Телефон", max_length=255)
    message = models.CharField(
        max_length=2500, blank=True, null=True, verbose_name="Сообщение"
    )
    agree = models.BooleanField("Согласие", default=False)
    verified = models.BooleanField("Проверен", default=False)

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"

    def __str__(self):
        return f"Обратная связь от {self.name} от {self.created_at}"


class Footer(models.Model):
    site_name = models.CharField(
        max_length=100, default="AlfaSms", verbose_name="Название сайта"
    )
    copyright = models.CharField(
        "Копирайт", max_length=255, default="© 2025 DVFitness. All rights reserved."
    )

    def __str__(self):
        return f"Футер"

    class Meta:
        verbose_name = "Футер"
        verbose_name_plural = "Футер"


class FooterLink(models.Model):
    """
    Модель ссылок футера
    """

    footer = models.ForeignKey(
        Footer, on_delete=models.CASCADE, related_name="links", verbose_name="Футер"
    )
    name = models.CharField("Название", max_length=255)

    class Meta:
        verbose_name = "Ссылка футера"
        verbose_name_plural = "Ссылки футера"

    def __str__(self):
        return f"Элемент футера {self.name}"


class FooterLinkItem(models.Model):
    """
    Модель элементов для ссылок футера
    """

    link = models.ForeignKey(
        FooterLink,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name="Ссылка футера",
    )
    name = models.CharField("Название", max_length=255)
    url = models.CharField("Ссылка", max_length=255)

    class Meta:
        verbose_name = "Элемент ссылки футера"
        verbose_name_plural = "Элементы ссылок футера"

    def __str__(self):
        return f"Элемент футера {self.name}"
