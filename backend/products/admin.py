from django.contrib import admin
from common.mixins import AdminImagePreviewMixin, AdminLimitMixin
from .models import (
    ProductVariant,
    ProductImage,
    Product,
    Category,
    Discount,
    ProductLike,
)
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from django.db.models import Q, Sum


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


class ProductImageLine(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductVariantLine(admin.TabularInline):
    model = ProductVariant
    extra = 1


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "name"  # поле, по которому делается отступ для вложенности
    list_display = (
        "tree_actions",  # стрелочки для раскрытия/сворачивания дерева
        "indented_title",  # название с отступом
        "slug",
        "is_active",
    )
    list_display_links = ("indented_title",)  # по клику на название — редактирование
    prepopulated_fields = {"slug": ("name",)}  # автозаполнение slug из name


@admin.register(Product)
class ProductAdmin(AdminImagePreviewMixin, admin.ModelAdmin):
    """Админка товаров"""

    image_field_name = "avatar"

    inlines = [ProductVariantLine, ProductImageLine]

    list_display = (
        "id",
        "brand",
        "country",
        "title",
        "category",
        "price",
        "currency",
        "is_active",
        "get_count_likes",
        "get_count_reviews",
        "get_count",
        "get_image",
    )
    fields = (
        ("brand", "country"),
        ("title", "category"),
        ("avatar", "description"),
        ("price", "currency"),
        "is_active",
    )
    save_on_top = True

    def get_count_likes(self, obj):
        return obj.likes.count()

    def get_count_reviews(self, obj):
        return obj.reviews.count()

    def get_count(self, obj):
        return obj.variants.aggregate(Sum("quantity")).get("quantity__sum", 0)

    get_count_likes.short_description = "Лайки"
    get_count_reviews.short_description = "Отзывы"
    get_count.short_description = "Количество"
