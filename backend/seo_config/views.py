from rest_framework.generics import RetrieveAPIView
from .models import SEO
from .serializers import SEOSerializer
from drf_spectacular.utils import extend_schema
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


TAG = "Настройки SEO и Конфигурация"


@extend_schema(tags=[TAG], summary="Получение SEO")
class SEOView(RetrieveAPIView):
    queryset = SEO.objects.all()
    serializer_class = SEOSerializer
    lookup_field = "slug"

    # @method_decorator(cache_page(60 * 10))  # кэш 10 минут
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)
