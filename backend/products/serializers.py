from rest_framework import serializers
from .models import (
    Category,
    Cart,
    CartItem,
    Favorite,
    Product,
    ProductVariant,
    ProductImage,
    Review,
    ReviewPhoto,
    ProductDetail,
    # Favorite,
    Brand,
)
from django.db.models import Sum


class RecursiveSerializer(serializers.Serializer):
    """Сериализатор для рекурсивного вывода детей"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CategoryListSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True, read_only=True)
    # image = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ("id", "name", "slug", "image", "children", "is_active")

    # def get_image(self, obj):
    #     if obj.image:
    #         return {
    #             "original": obj.image.url,
    #             "webp": (
    #                 obj.image_webp.url
    #                 if hasattr(obj, "image_webp") and obj.image_webp
    #                 else None
    #             ),
    #         }
    #     return None


class CategoryDetailSerializer(CategoryListSerializer):
    """Для детального просмотра, если нужно больше полей"""

    parent = serializers.SerializerMethodField()

    class Meta(CategoryListSerializer.Meta):
        fields = CategoryListSerializer.Meta.fields + ("parent",)

    def get_parent(self, obj):
        if obj.parent:
            return {
                "id": obj.parent.id,
                "name": obj.parent.name,
                "slug": obj.parent.slug,
            }
        return None


class BrandSerializer(serializers.ModelSerializer):
    """
    Сериализатор бренда
    """

    class Meta:
        model = Brand
        fields = "__all__"


class ProductVariantSerializer(serializers.ModelSerializer):
    """
    Сериализатор варианта товара
    """

    color_name = serializers.CharField(source="get_color_display")

    class Meta:
        model = ProductVariant
        fields = ("color", "color_name", "size", "quantity")


class ProductImageSerializer(serializers.ModelSerializer):
    """
    Сериализатор изображения товара
    """

    class Meta:
        model = ProductImage
        fields = ("id", "image")


class ProductReviewSerializer(serializers.ModelSerializer):
    """
    Сериализатор отзыва о товаре
    """

    class Meta:
        model = Review
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    """
    Сериализатор отзыва о товаре
    """

    time_age = serializers.ReadOnlyField()

    class Meta:
        model = Review
        fields = (
            "id",
            "user",
            "name",
            "email",
            "description",
            "product",
            "advantages",
            "disadvantages",
            "rating",
            "time_age",
            "created_at",
            "updated_at"
        )


class ProductDetailSerializer(serializers.ModelSerializer):
    """
    Дополнительные сведения о товаре
    """

    class Meta:
        model = ProductDetail
        fields = ("id", "title", "description")


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор продукта
    """

    details = ProductDetailSerializer(many=True, read_only=True)
    variants = ProductVariantSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    category = serializers.CharField(source="category.name")
    brand = BrandSerializer(read_only=True)
    currency = serializers.CharField(source="get_currency_display")
    count_likes = serializers.SerializerMethodField()
    count_reviews = serializers.SerializerMethodField()
    total_count = serializers.SerializerMethodField()

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
            "category",
            "count_likes",
            "count_reviews",
            "total_count",
            "images",
            "reviews",
            "variants",
            "details",
        )

    def get_count_likes(self, obj):
        return obj.likes.count()

    def get_count_reviews(self, obj):
        return obj.reviews.count()

    def get_total_count(self, obj):
        return obj.variants.aggregate(Sum("quantity")).get("quantity__sum", 0)


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
