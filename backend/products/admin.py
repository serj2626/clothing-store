from django.contrib import admin
from products.models import ProductVariant, ProductImage, Product, Category


class ProductImageLine(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductVariantLine(admin.TabularInline):
    model = ProductVariant
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Категории
    """

    list_display = ("name", "slug", "parent")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админка товаров"""

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
