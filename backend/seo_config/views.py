from rest_framework.generics import RetrieveAPIView
from .models import SEO
from .serializers import SEOSerializer
from drf_spectacular.utils import extend_schema
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.http import HttpResponse
from .models import RobotsTxt


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
