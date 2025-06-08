from rest_framework import serializers
from .models import (
    Category,
    Cart,
    CartItem,
    Product,
    ProductVariant,
    ProductImage,
    ProductReview,
    Favorite,
    Brand,
)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "slug", "image")


class CategoryDetailSerializer(CategorySerializer):
    children = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ("id", "name", "slug", "children")


class ProductVariantSerializer(serializers.ModelSerializer):
    color = serializers.CharField(source="get_color_display")

    class Meta:
        model = ProductVariant
        fields = ("color", "size", "quantity")


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = "__all__"


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    reviews = ProductReviewSerializer(many=True, read_only=True)
    category = serializers.CharField(source="category.name")
    brand = BrandSerializer(read_only=True)
    currency = serializers.CharField(source="get_currency_display")
    count_likes = serializers.SerializerMethodField()
    count_reviews = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "id",
            "brand",
            "title",
            "category",
            "avatar",
            "price",
            "currency",
            "is_active",
            "variants",
            "images",
            "reviews",
            "category",
            "count_likes",
            "count_reviews",
        )

    def get_count_likes(self, obj):
        return obj.likes.count()

    def get_count_reviews(self, obj):
        return obj.reviews.count()


class FavoriteSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Favorite
        fields = ["id", "product"]


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ["id", "product", "quantity"]


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ["items", "created_at", "updated_at"]
