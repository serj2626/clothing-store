from django.contrib import admin

from .models import (
    FAQ,
    Contact,
    Feedback,
    Footer,
    FooterLink,
    FooterLinkItem,
    Subscription,
)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    """
    Админка вопросов и ответов
    """

    list_display = ("question", "answer")


class FooterItemLinkInline(admin.TabularInline):
    model = FooterLinkItem
    extra = 1


@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    """
    Админка ссылок футера
    """

    list_display = ("name",)
    inlines = [FooterItemLinkInline]


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    """
    Админка подписки
    """

    list_display = ("email", "created_at", "verified")


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    """
    Админка футера
    """

    list_display = ("site_name", "copyright")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Админка контактов
    """

    list_display = ("type", "value")
    search_fields = ("type", "value")


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """
    Админка обратной связи
    """

    list_display = (
        "name",
        "phone",
        "agree",
        "verified",
    )
    search_fields = ("name", "phone")
