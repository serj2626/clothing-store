from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from common.models import BaseDate, BaseID
from products.models import Product

User = get_user_model()


class Cart(BaseID, BaseDate):
    """
    Корзина
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="cart",
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
        Cart,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name="Корзина",
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


# ===== ЗАКАЗ =====
class Order(BaseID):
    """
    Модель заказа
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="orders",
    )
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name="Дата создания"
    )
    paid = models.BooleanField(default=False, verbose_name="Оплачен")
    stripe_checkout_id = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Stripe checkout ID"
    )

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ No{self.id}"


class OrderItem(BaseID):
    """
    Позиция в заказе
    """

    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="items", verbose_name="Заказ"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")

    class Meta:
        verbose_name = "Позиция в заказе"
        verbose_name_plural = "Позиции в заказе"

    def __str__(self):
        return f"Позиция No{self.id} в заказе No{self.order.id}"
