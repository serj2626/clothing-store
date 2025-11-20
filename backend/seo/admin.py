from django.contrib import admin

from .models import SEO, RobotsTXT, Webmaster


@admin.register(Webmaster)
class WebmasterAdmin(admin.ModelAdmin):
    list_display = ("type", "text", "title")


@admin.register(RobotsTXT)
class RobotsTXTAdmin(admin.ModelAdmin):
    list_display = ("text",)


@admin.register(SEO)
class SEOAdmin(admin.ModelAdmin):
    list_display = (
        "slug",
        "title",
        "canonical_url",
        "noindex",
        "nofollow",
        "has_json_ld",
    )
    search_fields = ("slug", "title", "keywords")
    list_editable = ("canonical_url", "noindex", "nofollow")
    save_on_top = True
    readonly_fields = ("lastmod",)

    def has_json_ld(self, obj):
        return bool(obj.json_ld)

    has_json_ld.short_description = "JSON-LD"

    fieldsets = (
        ("Базовое", {"fields": ("slug", "title", "description", "keywords")}),
        ("Доп", {"fields": ("canonical_url", "noindex", "nofollow")}),
        (
            "Open Graph (соцсети)",
            {
                "fields": (
                    "og_title",
                    "og_description",
                    "og_image",
                    "og_site_name",
                    "og_type",
                )
            },
        ),
        ("JSON-LD", {"fields": ("json_ld",)}),
        (
            "Sitemap",
            {
                "fields": (
                    "priority",
                    "changefreq",
                    "lastmod",
                )  # lastmod останется, но будет readonly
            },
        ),
    )