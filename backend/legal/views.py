from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_spectacular.utils import extend_schema

from common.mixins import BaseSectionViewMixin

from .models import About, CookiePolicy, ExchangeAndReturnPage, Offerta, Policy
from .serializers import (
    AboutSerializer,
    CookiePolicySerializer,
    ExchangeAndReturnPageSerializer,
    OffertaSerializer,
    PolicySerializer,
)

TAG = "Юридическая информация"


@method_decorator(cache_page(60 * 15), name="get")
class AboutView(BaseSectionViewMixin):
    model = About
    serializer_class = AboutSerializer

    @extend_schema(tags=[TAG], summary="О компании")
    def get(self, request):
        return super().get(request)


@method_decorator(cache_page(60 * 15), name="get")
class OffertaView(BaseSectionViewMixin):
    model = Offerta
    serializer_class = OffertaSerializer

    @extend_schema(tags=[TAG], summary="Оферта")
    def get(self, request):
        return super().get(request)


@method_decorator(cache_page(60 * 15), name="get")
class PolicyView(BaseSectionViewMixin):
    model = Policy
    serializer_class = PolicySerializer

    @extend_schema(tags=[TAG], summary="Политика конфиденциальности")
    def get(self, request):
        return super().get(request)


@method_decorator(cache_page(60 * 15), name="get")
class CookiePolicyView(BaseSectionViewMixin):
    model = CookiePolicy
    serializer_class = CookiePolicySerializer

    @extend_schema(tags=[TAG], summary="Политика cookie")
    def get(self, request):
        return super().get(request)


@method_decorator(cache_page(60 * 15), name="get")
class ExchangeAndReturnPageView(BaseSectionViewMixin):
    model = ExchangeAndReturnPage
    serializer_class = ExchangeAndReturnPageSerializer

    @extend_schema(tags=[TAG], summary="Страница обмена и возврата")
    def get(self, request):
        return super().get(request)
