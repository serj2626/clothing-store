from django.db.models import Sum
from rest_framework import serializers
from common.utils import RelativeOnlyImageField
from common.utils import get_client_ip

from .models import (  # Favorite,
    Brand,
    Category,
    Favorite,
    Product,
    ProductLike,
    ProductVariant,
)


class RecursiveSerializer(serializers.Serializer):
    """Сериализатор для рекурсивного вывода детей"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CategoryListSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True, read_only=True)
    image = RelativeOnlyImageField()

    class Meta:
        model = Category
        fields = ("id", "name", "slug", "image", "children", "is_active")


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

    country = serializers.SerializerMethodField()
    image = RelativeOnlyImageField()

    class Meta:
        model = Brand
        fields = "__all__"

    def get_country(self, obj):
        return obj.get_country_display()


class ProductVariantSerializer(serializers.ModelSerializer):
    """
    Сериализатор варианта товара
    """

    color = serializers.CharField(source="color.title")
    color_code = serializers.CharField(source="color.color")
    status = serializers.SerializerMethodField()
    image = RelativeOnlyImageField()

    def get_status(self, obj):
        return 'В наличии' if obj.quantity > 0 else 'Нет в наличии'

    class Meta:
        model = ProductVariant
        fields = (
            "color",
            "color_code",
            "size",
            "quantity",
            'status',
            "image",
            "price",
        )


# class ProductReviewSerializer(serializers.ModelSerializer):
#     """
#     Сериализатор отзыва о товаре
#     """

#     class Meta:
#         model = Review
#         fields = "__all__"


# class ReviewPhotoSerializer(serializers.ModelSerializer):
#     """
#     Сериализатор фотографии отзыва о товаре
#     """

#     class Meta:
#         model = ReviewPhoto
#         fields = ("id", "image", "alt")


# class ReviewSerializer(serializers.ModelSerializer):
#     """
#     Сериализатор отзыва о товаре
#     """

#     time_age = serializers.ReadOnlyField()
#     photos = ReviewPhotoSerializer(many=True, read_only=True)

#     class Meta:
#         model = Review
#         fields = (
#             "id",
#             # "user",
#             "name",
#             "email",
#             "description",
#             # "product",
#             "advantages",
#             "disadvantages",
#             "rating",
#             "time_age",
#             "created_at",
#             "updated_at",
#             "photos",
#         )


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор продукта
    """

    liked = serializers.SerializerMethodField()
    variants = ProductVariantSerializer(many=True, read_only=True)
    # reviews = ReviewSerializer(many=True, read_only=True)
    category = serializers.CharField(source="category.name")
    brand = BrandSerializer(read_only=True)
    count_likes = serializers.SerializerMethodField()
    count_reviews = serializers.SerializerMethodField()
    total_count = serializers.SerializerMethodField()
    avatar = RelativeOnlyImageField()

    class Meta:
        model = Product
        fields = (
            "id",
            "brand",
            "title",
            "category",
            "avatar",
            "is_active",
            "category",
            "count_likes",
            "count_reviews",
            "total_count",
            # "reviews",
            "variants",
            "liked",
        )

    def get_count_likes(self, obj):
        return obj.likes.count()

    def get_count_reviews(self, obj):
        return obj.reviews.count()

    def get_total_count(self, obj):
        return obj.variants.aggregate(Sum("quantity")).get("quantity__sum", 0)

    def get_liked(self, obj):
        request = self.context.get("request")
        if not request:
            return False
        ip = get_client_ip(request)
        return ProductLike.objects.filter(product=obj, ip_address=ip).exists()


class FavoriteSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Favorite
        fields = ["id", "product"]


# class CartItemSerializer(serializers.ModelSerializer):
#     product = ProductSerializer(read_only=True)

#     class Meta:
#         model = CartItem
#         fields = ["id", "product", "quantity"]


# class CartSerializer(serializers.ModelSerializer):
#     items = CartItemSerializer(many=True, read_only=True)

#     class Meta:
#         model = Cart
#         fields = ["items", "created_at", "updated_at"]
