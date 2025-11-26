from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_spectacular.utils import extend_schema

from common.mixins import BaseSectionViewMixin
from common.utils import get_cache_ttl

from .models import About, CookiePolicy, ExchangeAndReturnPage, Offerta, Policy
from .serializers import (
    AboutSerializer,
    CookiePolicySerializer,
    ExchangeAndReturnPageSerializer,
    OffertaSerializer,
    PolicySerializer,
)

TAG = "Юридическая информация"


@extend_schema(tags=[TAG], summary="О компании")
@method_decorator(cache_page(get_cache_ttl(15)), name='dispatch')
class AboutView(BaseSectionViewMixin):
    model = About
    serializer_class = AboutSerializer


@extend_schema(tags=[TAG], summary="Оферта")
@method_decorator(cache_page(get_cache_ttl(15)), name='dispatch')
class OffertaView(BaseSectionViewMixin):
    model = Offerta
    serializer_class = OffertaSerializer


@extend_schema(tags=[TAG], summary="Политика конфиденциальности")
@method_decorator(cache_page(get_cache_ttl(15)), name='dispatch')
class PolicyView(BaseSectionViewMixin):
    model = Policy
    serializer_class = PolicySerializer


@extend_schema(tags=[TAG], summary="Политика cookie")
@method_decorator(cache_page(get_cache_ttl(15)), name='dispatch')
class CookiePolicyView(BaseSectionViewMixin):
    model = CookiePolicy
    serializer_class = CookiePolicySerializer


@extend_schema(tags=[TAG], summary="Страница обмена и возврата")
@method_decorator(cache_page(get_cache_ttl(15)), name='dispatch')
class ExchangeAndReturnPageView(BaseSectionViewMixin):
    model = ExchangeAndReturnPage
    serializer_class = ExchangeAndReturnPageSerializer
