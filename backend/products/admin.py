from django.contrib import admin
from common.mixins import AdminImagePreviewMixin, AdminLimitMixin
from .models import ProductVariant, ProductImage, Product, Category, Discount
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin


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
        "title",
        "category",
        "avatar",
        "price",
        "currency",
        "is_active",
    )
    fields = (
        ("title", "category"),
        ("avatar", "description"),
        ("price", "currency"),
        "is_active",
    )
    save_on_top = True
