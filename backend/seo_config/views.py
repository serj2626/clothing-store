import datetime
from rest_framework.generics import RetrieveAPIView
from .serializers import SEOSerializer, RobotsTxtSerializer, SitemapItemSerializer
from drf_spectacular.utils import extend_schema
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.http import HttpResponse
from .models import RobotsTxt
from rest_framework import viewsets, generics
from products.models import Product, Category
from django.contrib.sitemaps import Sitemap
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import SEO, RobotsTxt, SitemapItem
from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.openapi import OpenApiResponse

TAG = "Настройки SEO и Конфигурация"


def robots_txt_view(request):
    robots = RobotsTxt.objects.filter(is_active=True).first()
    content = robots.content if robots else "User-agent: *\nDisallow: /"
    return HttpResponse(content, content_type="text/plain")


@extend_schema(tags=[TAG], summary="Получение SEO")
class SEOView(RetrieveAPIView):
    queryset = SEO.objects.all()
    serializer_class = SEOSerializer
    lookup_field = "slug"

    # @method_decorator(cache_page(60 * 10))  # кэш 10 минут
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


class RobotsTxtViewSet(generics.ListAPIView):
    serializer_class = RobotsTxtSerializer

    def get_queryset(self):
        return RobotsTxt.objects.filter(is_active=True)

    @extend_schema(tags=[TAG], summary="robots.txt")
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.get_serializer(queryset.first())
            return Response(serializer.data)
        # Возвращаем дефолтный robots.txt, если нет активного
        return Response({"content": "User-agent: *\nDisallow:", "is_active": True})


class SitemapViewSet(generics.ListAPIView):
    serializer_class = SitemapItemSerializer

    def get_queryset(self):
        queryset = SitemapItem.objects.filter(is_active=True).order_by("-priority")

        # Опциональные фильтры через query params
        changefreq = self.request.query_params.get("changefreq", None)
        if changefreq:
            queryset = queryset.filter(changefreq=changefreq)

        return queryset

    @extend_schema(
        tags=["SEO"],
        summary="Получить карту сайта",
        description="Возвращает список активных URL для карты сайта, отсортированных по приоритету",
        # parameters=[
        #     OpenApiParameter(
        #         name="changefreq",
        #         description="Фильтр по частоте обновления",
        #         required=False,
        #         type=str,
        #         enum=[freq[0] for freq in SitemapItem.ChangeFrequency.choices],
        #     ),
        # ],
        responses={
            200: SitemapItemSerializer(many=True),
            404: OpenApiResponse(description="Not Found"),
        },
    )
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if not queryset.exists():
            return Response({"detail": "No active sitemap items found"}, status=404)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
