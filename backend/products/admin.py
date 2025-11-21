from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from mptt.admin import DraggableMPTTAdmin

from common.mixins import (
    AdminImagePreviewMixin,
    AdminShortDescriptionMixin,
    AvatarPreviewMixin,
)

from .models import (
    Brand,
    Category,
    Discount,
    Product,
    ProductColor,
    ProductLike,
    ProductSize,
    ProductVariant,
)


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


@admin.register(ProductLike)
class ProductLikeAdmin(admin.ModelAdmin):
    """
    Админка лайков
    """

    list_display = (
        "product",
        "ip_address",
        "created_at",
    )


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
    fields = ("color", "size", "price", "quantity", "image", "avatar_preview")


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "name"  # поле, по которому делается отступ для вложенности
    list_display = (
        "tree_actions",  # стрелочки для раскрытия/сворачивания дерева
        "indented_title",  # название с отступом
        "is_active",
        'slug',
        "get_image",
    )
    list_display_links = ("indented_title",)  # по клику на название — редактирование
    prepopulated_fields = {"slug": ("name",)}  # автозаполнение slug из name

    def get_image(self, obj):
        if obj.image and obj.parent is None:
            return mark_safe(
                f'<img src="{obj.image.url}" style="border-radius: 50%;" width="50" height="50">'
            )
        return "---"

    get_image.short_description = "Фото"


@admin.register(Product)
class ProductAdmin(AvatarPreviewMixin, admin.ModelAdmin):
    """Админка товаров"""

    image_field_name = "avatar"
    inlines = [
        ProductVariantInline,
    ]
    list_display = (
        "sku",
        "get_title",
        "brand",
        "gender",
        "category",
        "is_active",
        "get_count_likes",
        "get_count_reviews",
        "avatar_preview",
    )
    readonly_fields = ("avatar_preview",)
    fields = (
        ("brand", "gender"),
        ("title", "category"),
        "sku",
        "is_active",
        "avatar",
        'avatar_preview',
    )
    save_on_top = True
    list_per_page = 15
    list_filter = (
        "brand",
        "category",
    )
    list_editable = ("is_active", "gender", "brand")
    search_fields = ('sku', "title", "brand__name", "brand__country")
    ordering = ["category"]

    def get_count_likes(self, obj):
        return obj.likes.count()

    def get_title(self, obj):
        return f"{obj.title[:20]}..."

    def get_count_reviews(self, obj):
        return obj.reviews.count() if obj.reviews else 0

    # def get_count(self, obj):
    #     return obj.variants.aggregate(Sum("quantity")).get("quantity__sum", 0)

    get_count_likes.short_description = "Лайки"
    get_count_reviews.short_description = "Отзывы"
    # get_count.short_description = "Количество"
    get_title.short_description = "Название"
