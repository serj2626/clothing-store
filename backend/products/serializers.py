from django.db.models import Sum
from rest_framework import serializers

from common.utils import RelativeOnlyImageField

from .models import Brand, Category, Favorite, Product, ProductVariant  # Favorite,


class RecursiveSerializer(serializers.Serializer):
    """Сериализатор для рекурсивного вывода детей"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CategoryListSerializer(serializers.ModelSerializer):
    # children = RecursiveSerializer(many=True, read_only=True)
    image = RelativeOnlyImageField()

    class Meta:
        model = Category
        # fields = ("id", "name", "slug", "image", "children", "is_active")
        fields = ("id", "name", "slug", "image", "is_active")


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
    size = serializers.CharField(source="size.title")

    def get_status(self, obj):
        return 'В наличии' if obj.quantity > 0 else 'Нет в наличии'

    class Meta:
        model = ProductVariant
        fields = (
            'id',
            "color",
            "color_code",
            "size",
            "quantity",
            'status',
            "image",
        )


class ProductLastListSerializer(serializers.ModelSerializer):
    """
    Сериализатор последнего списка продуктов
    """

    brand = serializers.SlugRelatedField(slug_field="name", read_only=True)
    avatar = RelativeOnlyImageField()

    class Meta:
        model = Product
        fields = (
            "id",
            "brand",
            "title",
            "avatar",
            "is_active",
            'sku',
            'price',
        )

class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор продукта
    """

    # liked = serializers.SerializerMethodField()
    variants = ProductVariantSerializer(many=True, read_only=True)
    # reviews = ReviewSerializer(many=True, read_only=True)
    category = serializers.CharField(source="category.name")
    brand = BrandSerializer(read_only=True)
    # count_likes = serializers.SerializerMethodField()
    # count_reviews = serializers.SerializerMethodField()
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
            # "count_likes",
            # "count_reviews",
            "total_count",
            'sku',
            'price',
            "variants",
        )

    # def get_count_likes(self, obj):
    #     return obj.likes.count()

    # def get_count_reviews(self, obj):
    #     return obj.reviews.count()

    def get_total_count(self, obj):
        return obj.variants.aggregate(Sum("quantity")).get("quantity__sum", 0)

    # def get_liked(self, obj):
    #     request = self.context.get("request")
    #     if not request:
    #         return False
    #     ip = get_client_ip(request)
    #     return ProductLike.objects.filter(product=obj, ip_address=ip).exists()


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
