from common.mixins import BaseSectionViewMixin
from .models import About, CookiePolicy, Offerta, Policy, ExchangeAndReturnPage
from .serializers import (
    AboutSerializer,
    CookiePolicySerializer,
    OffertaSerializer,
    PolicySerializer,
    ExchangeAndReturnPageSerializer,
)
from drf_spectacular.utils import extend_schema
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response


TAG = "Юридическая информация"


class AboutView(BaseSectionViewMixin):
    model = About
    serializer_class = AboutSerializer

    @extend_schema(tags=[TAG], summary="О компании")
    def get(self, request):
        return super().get(request)


class OffertaView(BaseSectionViewMixin):
    model = Offerta
    serializer_class = OffertaSerializer

    @extend_schema(tags=[TAG], summary="Оферта")
    def get(self, request):
        return super().get(request)


class PolicyView(BaseSectionViewMixin):
    model = Policy
    serializer_class = PolicySerializer

    @extend_schema(tags=[TAG], summary="Политика конфиденциальности")
    def get(self, request):
        return super().get(request)


class CookiePolicyView(BaseSectionViewMixin):
    model = CookiePolicy
    serializer_class = CookiePolicySerializer

    @extend_schema(tags=[TAG], summary="Политика cookie")
    def get(self, request):
        return super().get(request)


class ExchangeAndReturnPageView(BaseSectionViewMixin):
    model = ExchangeAndReturnPage
    serializer_class = ExchangeAndReturnPageSerializer

    @extend_schema(tags=[TAG], summary="Страница обмена и возврата")
    def get(self, request):
        return super().get(request)
