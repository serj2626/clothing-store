from django.db import models
from django.utils.text import slugify
from common.types import POST_CATEGORY_TYPES
from common.models import BaseContent, BaseID, BaseTitle, BaseDate


class Offerta(BaseTitle, BaseContent):
    """
    Оферта
    """

    class Meta:
        verbose_name = "Оферта"
        verbose_name_plural = "Оферта"

    def __str__(self):
        return f'Оферта "{self.title}"'


class Policy(BaseTitle, BaseContent):
    """
    Политика конфиденциальности
    """

    class Meta:
        verbose_name = "Политика конфиденциальности"
        verbose_name_plural = "Политика конфиденциальности"

    def __str__(self):
        return f"Политика конфиденциальности '{self.title}'"


class CookiePolicy(BaseTitle, BaseContent):
    """
    Политика cookie
    """

    class Meta:
        verbose_name = "Политика cookie"
        verbose_name_plural = "Политика cookie"

    def __str__(self):
        return f'Политика cookie "{self.title}"'

    class Meta:
        verbose_name = "Политика cookie"
        verbose_name_plural = "Политика cookie"


class About(BaseTitle, BaseContent):
    """
    О нас
    """

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

    def __str__(self):
        return f'О нас "{self.title}"'

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"


class Post(BaseID, BaseTitle, BaseContent, BaseDate):
    """
    Модель поста
    """

    category = models.CharField(
        "Категория", max_length=100, choices=POST_CATEGORY_TYPES, default="hands"
    )
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class PaymentAndDeliveryPage(BaseDate):
    """
    Модель страницы Оплата и Доставка
    """

    title = models.CharField("Заголовок", max_length=100)

    class Meta:
        verbose_name = "Страница Оплата и Доставка"
        verbose_name_plural = "Страницы Оплата и Доставка"

    def __str__(self):
        return f'Страница "{self.title}"'


class PaymentVariant(BaseTitle):
    """
    Модель вариантов оплаты
    """

    page = models.ForeignKey(
        PaymentAndDeliveryPage,
        on_delete=models.CASCADE,
        verbose_name="Страница",
        related_name="payment_variants",
    )

    class Meta:
        verbose_name = "Вариант оплаты"
        verbose_name_plural = "Варианты оплаты"


class PaymentVariantValues(models.Model):
    """
    Модель значений вариантов оплаты
    """

    text = models.TextField("Текст")
    payment_variant = models.ForeignKey(
        PaymentVariant, on_delete=models.CASCADE, verbose_name="Вариант оплаты"
    )

    class Meta:
        verbose_name = "Вариант оплаты"
        verbose_name_plural = "Варианты оплаты"


class DeliveryVariant(BaseTitle):
    """
    Модель вариантов доставки
    """

    page = models.ForeignKey(
        PaymentAndDeliveryPage,
        on_delete=models.CASCADE,
        verbose_name="Страница",
        related_name="delivery_variants",
    )

    class Meta:
        verbose_name = "Вариант оплаты"
        verbose_name_plural = "Варианты оплаты"


class DeliveryVariantValues(models.Model):
    """
    Модель значений вариантов доставки
    """

    text = models.TextField("Текст")
    delivery_variant = models.ForeignKey(
        DeliveryVariant, on_delete=models.CASCADE, verbose_name="Вариант доставки"
    )

    class Meta:
        verbose_name = "Вариант доставки"
        verbose_name_plural = "Варианты доставки"


class OrderingProcess(BaseDate):
    """
    Модель процесса заказа
    """

    title = models.CharField("Заголовок", max_length=100)
    page = models.ForeignKey(
        PaymentAndDeliveryPage,
        on_delete=models.CASCADE,
        verbose_name="Страница",
        related_name="ordering_processes",
    )

    class Meta:
        verbose_name = "Процесс заказа"
        verbose_name_plural = "Процессы заказа"

    def __str__(self):
        return self.title


class OrderingProcessItem(models.Model):
    """
    Модель пунктов процесса заказа
    """

    text = models.TextField("Текст")
    icon = models.FileField(
        "Иконка", upload_to="ordering_process_icons/", blank=True, null=True
    )
    ordering_process = models.ForeignKey(
        OrderingProcess, on_delete=models.CASCADE, verbose_name="Процесс заказа"
    )

    class Meta:
        verbose_name = "Пункт процесса заказа"
        verbose_name_plural = "Пункты процесса заказа"

    def __str__(self):
        return f'Пункт "{self.text}"'


class ExchangeAndReturnPage(BaseTitle, BaseDate):
    """
    Модель страницы Обмен и Возврат
    """

    description = models.TextField("Описание")
    text = models.TextField("Текст")

    class Meta:
        verbose_name = "Страница Обмен и Возврат"
        verbose_name_plural = "Страницы Обмен и Возврат"

    def __str__(self):
        return f'Страница "{self.title}"'


class TermsProcessItem(models.Model):
    """
    Модель пунктов процесса заказа
    """

    page = models.ForeignKey(
        ExchangeAndReturnPage,
        on_delete=models.CASCADE,
        verbose_name="Страница",
        related_name="terms_processes_items",
    )
    text = models.TextField("Текст")
    icon = models.FileField(
        "Иконка", upload_to="terms_process_icons/", blank=True, null=True
    )

    class Meta:
        verbose_name = "Пункт процесса заказа"
        verbose_name_plural = "Пункты процесса заказа"

    def __str__(self):
        return f'Пункт "{self.text}"'
