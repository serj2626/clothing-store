import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import filters, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from common.pagination import ListResultsSetPagination

from .filters import ProductFilter
from .models import Brand, Category, Favorite, Product
from .serializers import (
    BrandSerializer,
    CategoryBySlugSerializer,
    CategoryDetailSerializer,
    CategoryListSerializer,
    FavoriteSerializer,
    ProductLastListSerializer,
    ProductSerializer,
)

stripe.api_key = settings.STRIPE_SECRET_KEY


TAG = "Товары и Корзина"


@extend_schema(tags=["Категории"], summary="Список кат")
# @method_decorator(cache_page(get_cache_ttl()), name='dispatch')
class CategoryListBySlugView(generics.RetrieveAPIView):
    """Возвращает категорию + всё её дерево дочерних категорий"""

    serializer_class = CategoryBySlugSerializer
    lookup_field = "slug"
    queryset = Category.objects.all()


@extend_schema(tags=[TAG], summary="Список брендов")
# @method_decorator(cache_page(get_cache_ttl()), name='dispatch')
class BrandListView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


@extend_schema(tags=["Категории"], summary="Список категорий")
# @method_decorator(cache_page(get_cache_ttl()), name='dispatch')
class CategoryListView(generics.ListAPIView):
    """Список всех категорий с древовидной структурой"""

    serializer_class = CategoryListSerializer

    def get_queryset(self):
        return Category.objects.filter(parent__isnull=True).all()


@extend_schema(tags=["Категории"], summary="Детали категории")
# @method_decorator(cache_page(get_cache_ttl(10)), name='dispatch')
class CategoryDetailView(generics.RetrieveAPIView):
    """Детальная информация о категории"""

    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = "slug"


# @extend_schema(tags=[TAG], summary="Поставить лайк товару")
# @api_view(["POST"])
# def toggle_product_like(request, product_id):
#     ip = get_client_ip(request)
#     product = Product.objects.get(id=product_id)

#     like, created = ProductLike.objects.get_or_create(product=product, ip_address=ip)

#     if not created:
#         like.delete()
#         liked = False
#     else:
#         liked = True

#     total_likes = ProductLike.objects.filter(product=product).count()
#     return JsonResponse({"liked": liked, "total_likes": total_likes})


@extend_schema(
    tags=[TAG],
    summary="Последние добавленные товары",
    description="Возвращает последние 10 товаров",
)
# @method_decorator(cache_page(get_cache_ttl()), name='dispatch')
class ProductLastCollectionView(generics.ListAPIView):
    queryset = (
        Product.objects.all()
        .select_related("brand", 'category')
        .order_by("-created_at")[:10]
    )
    serializer_class = ProductLastListSerializer


@extend_schema(tags=[TAG], summary="Список товаров по слагу категории")
# @method_decorator(cache_page(get_cache_ttl(10)), name='dispatch')
class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = ListResultsSetPagination

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        category = Category.objects.get(slug=slug)
        categories = category.get_descendants(include_self=True)

        return (
            Product.objects.filter(category__in=categories)
            .select_related("brand", 'category')
            .prefetch_related("variants")
            .order_by('price')
            .all()
        )


class ProductExampleListView(generics.ListAPIView):
    queryset = Product.objects.select_related("brand", 'category').all()
    serializer_class = ProductSerializer
    pagination_class = ListResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = ProductFilter
    ordering_fields = ["price", "created_at"]
    ordering = ["price"]

    @extend_schema(
        tags=[TAG],
        summary="Список товаров",
        parameters=[
            OpenApiParameter("price_min", OpenApiTypes.NUMBER, description="Цена от"),
            OpenApiParameter("price_max", OpenApiTypes.NUMBER, description="Цена до"),
            OpenApiParameter("category", OpenApiTypes.INT, description="ID категории"),
            OpenApiParameter("brand", OpenApiTypes.INT, description="ID бренда"),
            OpenApiParameter(
                "gender",
                OpenApiTypes.STR,
                description="Пол ('male', 'female', 'unisex')",
            ),
            OpenApiParameter(
                "ordering",
                OpenApiTypes.STR,
                description="Сортировка (например: price, -price)",
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


@extend_schema(tags=[TAG], summary="Детали товара")
# @method_decorator(cache_page(get_cache_ttl(10)), name='dispatch')
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context


# ===== ИЗБРАННОЕ =====
class FavoriteView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = Favorite.objects.filter(user=request.user)
        data = FavoriteSerializer(items, many=True).data
        return Response(data)

    def post(self, request):
        product_id = request.data.get("product_id")
        product = get_object_or_404(Product, id=product_id)
        Favorite.objects.get_or_create(user=request.user, product=product)
        return Response({"status": "added"})
