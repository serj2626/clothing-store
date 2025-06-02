from django.conf import settings
from django.db import models
from django.utils import timezone
from common.models import BaseID
from products.models import Product

# from django.db import models

# from products.models import Cart
# from users.models import User


# class Order(models.Model):
#     """
#     Модель заказа
#     """

#     CREATED = 0
#     PAID = 1
#     ON_WAY = 2
#     DELIVERED = 3
#     STATUSES = (
#         (CREATED, "Создан"),
#         (PAID, "Оплачен"),
#         (ON_WAY, "В пути"),
#         (DELIVERED, "Доставлен"),
#     )

#     first_name = models.CharField(max_length=64)
#     last_name = models.CharField(max_length=64)
#     email = models.EmailField(max_length=256)
#     address = models.CharField(max_length=256)
#     basket_history = models.JSONField(default=dict)
#     created = models.DateTimeField(auto_now_add=True)
#     status = models.SmallIntegerField(default=CREATED, choices=STATUSES)
#     initiator = models.ForeignKey(to=User, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"Order #{self.id}. {self.first_name} {self.last_name}"

#     def update_after_payment(self):
#         baskets = Cart.objects.filter(user=self.initiator)
#         self.status = self.PAID
#         self.basket_history = {
#             "purchased_items": [basket.de_json() for basket in baskets],
#             "total_sum": float(baskets.total_sum()),
#         }
#         baskets.delete()
#         self.save()


# ===== ЗАКАЗ =====
class Order(BaseID):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    paid = models.BooleanField(default=False)
    stripe_checkout_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ No{self.id}"


class OrderItem(BaseID):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Позиция в заказе"
        verbose_name_plural = "Позиции в заказе"

    def __str__(self):
        return f"Позиция No{self.id} в заказе No{self.order.id}"
