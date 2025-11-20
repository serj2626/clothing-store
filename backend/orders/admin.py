from django.contrib import admin

from .models import Cart, CartItem, Order, OrderItem


class CartItemInline(admin.TabularInline):
    """
    Класс админки позиций в корзине
    """

    model = CartItem
    extra = 3


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    '''Admin View for'''

    list_display = ('user', 'get_name', 'get_last_name', 'get_city')
    inlines = [CartItemInline]

    def get_name(self, obj):
        return obj.user.profile.first_name or 'Нет указано'

    def get_last_name(self, obj):
        return obj.user.profile.last_name or 'Нет указана'

    def get_city(self, obj):
        return obj.user.profile.city or 'Нет указан'

    get_name.short_description = 'Имя'
    get_last_name.short_description = 'Фамилия'
    get_city.short_description = 'Город'


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
