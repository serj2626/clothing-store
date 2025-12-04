from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin
from mptt.admin import DraggableMPTTAdmin, TreeRelatedFieldListFilter

from common.mixins import (
    AdminImagePreviewMixin,
    AdminShortDescriptionMixin,
    AvatarPreviewMixin,
)

from .models import (
    Brand,
    Category,
    CategoryCharacteristic,
    Discount,
    Product,
    ProductColor,
    ProductSize,
    ProductVariant,
)
from .resources import ProductResource


@admin.register(CategoryCharacteristic)
class CategoryCharacteristicAdmin(admin.ModelAdmin):
    '''Admin View for CategoryCharacteristic'''

    list_display = ('category', 'color', 'size')
    list_per_page = 20
    list_filter = ('category', 'color', 'size')
    list_filter = (
        ("category", TreeRelatedFieldListFilter),
        "color",
        "size",
    )
    search_fields = ('category__name', 'color__title', 'size__title')
    ordering = ["category"]


@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    '''Admin View for'''

    list_display = ('title', 'slug')


@admin.register(ProductColor)
class ProductColorAdmin(admin.ModelAdmin):
    '''Admin View for ProductColor'''

    list_display = ("title", "color", "color_preview", "slug")

    def color_preview(self, obj):
        if obj.color:
            return format_html(
                '<div style="background-color: {}; width: 30px; height: 30px; border-radius: 50%; display: inline-block;box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);"></div>',
                obj.color,
            )
        return "-"

    color_preview.short_description = "Предпросмотр цвета"


@admin.register(Brand)
class BrandAdmin(AdminImagePreviewMixin, AdminShortDescriptionMixin, admin.ModelAdmin):
    """
    Админка брендов
    """

    list_display = (
        "name",
        "country",
        "get_description",
        "slug",
        "get_image",
    )
    search_fields = ("name", "country")

    prepopulated_fields = {"slug": ("name",)}


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    """
    Админка скидок
    """

    list_display = (
        "amount",
        "start_date",
        "end_date",
        "is_active",
    )
    fields = (
        ("amount", "is_active"),
        ("start_date", "end_date"),
        "products",
        "categories",
    )

    filter_horizontal = ("products", "categories")


class ProductVariantInline(AvatarPreviewMixin, admin.TabularInline):
    model = ProductVariant
    extra = 1
    image_field_name = "image"

    readonly_fields = ("avatar_preview",)
    fields = ("color", "size", "quantity", "image", "avatar_preview")


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = (
        "tree_actions",
        "indented_title",
        "is_active",
        'slug',
        "get_image",
    )
    list_display_links = ("indented_title",)
    prepopulated_fields = {"slug": ("name",)}

    def get_image(self, obj):
        if obj.image and obj.parent is None:
            return mark_safe(
                f'<img src="{obj.image.url}" style="border-radius: 50%;" width="50" height="50">'
            )
        return "---"

    get_image.short_description = "Фото"


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin, AvatarPreviewMixin, admin.ModelAdmin):
    """Админка товаров"""

    resource_class = ProductResource
    image_height = 100

    image_field_name = "avatar"
    inlines = [
        ProductVariantInline,
    ]
    list_filter = (
        "brand",
        ("category", TreeRelatedFieldListFilter),
    )
    list_display = (
        "sku",
        "get_title",
        "brand",
        'price',
        "gender",
        "category",
        "is_active",
        "avatar_preview",
    )
    readonly_fields = ("avatar_preview",)

    fieldsets = (
        (
            "Основное",
            {
                "fields": (
                    ("brand", "gender"),
                    ("title", "category"),
                    ("sku", "price"),
                    "is_active",
                )
            },
        ),
        (
            "Изображение",
            {
                "fields": ("avatar", "avatar_preview"),
                "classes": ("collapse",),  # если хочешь свернуть
            },
        ),
    )

    save_on_top = True
    list_per_page = 15
    list_editable = ("is_active", 'price', "gender", "brand")
    search_fields = ('sku', "title", "brand__name", "brand__country")
    ordering = ["category"]

    def get_title(self, obj):
        return f"{obj.title[:20]}..."

    get_title.short_description = "Название"
