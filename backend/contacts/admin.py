from django.contrib import admin
from .models import Contact, Feedback, Footer


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
