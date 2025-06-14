from django.contrib import admin

from common.mixins import SingletonAdminInfoMixin
from .models import (
    About,
    Offerta,
    Policy,
    CookiePolicy,
    PaymentAndDeliveryPage,
    PaymentVariant,
    PaymentVariantValues,
    DeliveryVariant,
    DeliveryVariantValues,
    ExchangeAndReturnPage,
    TermsProcessItem,
)

class TermsProcessItemInline(admin.TabularInline):
    """
    Админка пунктов процесса заказа
    """
    
    model = TermsProcessItem
    extra = 3


@admin.register(ExchangeAndReturnPage)
class ExchangeAndReturnPageAdmin(admin.ModelAdmin):
    """
    Админка страницы обмена и возврата
    """

    list_display = ("title", "description", "text")
    inlines = [TermsProcessItemInline]


class PaymentVariantValuesInline(admin.TabularInline):
    model = PaymentVariantValues
    extra = 1


@admin.register(PaymentVariant)
class PaymentVariantAdmin(admin.ModelAdmin):
    """
    Админка вариантов оплаты
    """

    list_display = ("title",)
    inlines = [PaymentVariantValuesInline]


@admin.register(PaymentAndDeliveryPage)
class PaymentAndDeliveryPageAdmin(admin.ModelAdmin):
    """
    Админка страницы оплаты и доставки
    """

    list_display = ("title",)


@admin.register(About)
class AboutAdmin(SingletonAdminInfoMixin, admin.ModelAdmin):
    """
    Админка компании
    """

    list_display = ("title", "get_desc")


@admin.register(Offerta)
class OffertaAdmin(SingletonAdminInfoMixin, admin.ModelAdmin):
    """
    Админка оферты
    """

    list_display = ("title", "get_desc")


@admin.register(Policy)
class PolicyAdmin(SingletonAdminInfoMixin, admin.ModelAdmin):

    list_display = ("title", "get_desc")


@admin.register(CookiePolicy)
class CookiePolicyAdmin(SingletonAdminInfoMixin, admin.ModelAdmin):
    """
    Админка политики cookie
    """

    list_display = ("title", "get_desc")
