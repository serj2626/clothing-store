from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, RetrieveAPIView

from common.utils import get_cache_ttl

from .models import SEO, RobotsTXT
from .serializers import SEOSerializer

TAG = "Настройки SEO и Конфигурация"


@cache_page(get_cache_ttl())
def robots_txt_view(request):
    robots_obj = RobotsTXT.objects.first()
    content = robots_obj.text if robots_obj else "User-agent: *\nDisallow:"
    return HttpResponse(content, content_type="text/plain")


@extend_schema(tags=[TAG], summary="Получение SEO")
@method_decorator(cache_page(get_cache_ttl(10)), name='dispatch')
class SEOView(RetrieveAPIView):
    queryset = SEO.objects.all()
    serializer_class = SEOSerializer
    lookup_field = "slug"


@extend_schema(tags=[TAG], summary="Получение списка SEO")
class SEOListView(ListAPIView):
    queryset = SEO.objects.all()
    serializer_class = SEOSerializer
