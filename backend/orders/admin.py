from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    """
    Класс админки позиций в заказе
    """

    model = OrderItem
    extra = 3


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Класс админки заказов
    """

    list_display = (
        "user",
        "created_at",
        "paid",
        "stripe_checkout_id",
    )
    inlines = [OrderItemInline]
