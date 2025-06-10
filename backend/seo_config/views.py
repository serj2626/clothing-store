from rest_framework.generics import RetrieveAPIView
from .serializers import SEOSerializer, RobotsTxtSerializer, SitemapItemSerializer
from drf_spectacular.utils import extend_schema
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from .models import SEO, RobotsTxt, SitemapItem
from drf_spectacular.openapi import OpenApiResponse
from django.template.loader import render_to_string


TAG = "Настройки SEO и Конфигурация"


def robots_txt_view(request):
    robots = RobotsTxt.objects.filter(is_active=True).first()
    content = robots.content if robots else "User-agent: *\nDisallow: /"
    return HttpResponse(content, content_type="text/plain")


@extend_schema(tags=[TAG], summary="Получение списка SEO")
class SEOListView(generics.ListAPIView):
    queryset = SEO.objects.all()
    serializer_class = SEOSerializer


@extend_schema(tags=[TAG], summary="Получение SEO")
class SEODetailView(RetrieveAPIView):
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


def sitemap_xml(request):
    seo_items = SEO.objects.all()
    xml = render_to_string(
        "seo/sitemap.xml",
        {
            "items": seo_items,
            "request": request,
        },
    )
    return HttpResponse(xml, content_type="application/xml")


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
