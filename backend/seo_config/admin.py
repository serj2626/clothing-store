from django.contrib import admin
from .models import SEO, RobotsTxt

@admin.register(SEO)
class SEOAdmin(admin.ModelAdmin):
    list_display = ("slug", "title", "keywords")
    search_fields = ("slug", "title", "keywords")
    fieldsets = (
        ("Базовое", {
            "fields": ("slug", "title", "description", "keywords")
        }),
        ("Open Graph (соцсети)", {
            "fields": ("og_title", "og_description", "og_image")
        }),
        # ("Twitter Cards", {
        #     "fields": ("twitter_title", "twitter_description", "twitter_image")
        # }),
    )


@admin.register(RobotsTxt)
class RobotsTxtAdmin(admin.ModelAdmin):
    list_display = ("__str__", "is_active")