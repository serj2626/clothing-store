from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_spectacular.utils import extend_schema
from rest_framework import generics

from common.mixins import BaseSectionViewMixin
from common.pagination import ListResultsSetPagination
from common.utils import get_cache_ttl

from .models import FAQ, Contact, Feedback, Footer, Subscription
from .serializers import (
    ContactSerializer,
    FAQListSerializer,
    FeedbackSerializer,
    FooterSerializer,
    SubscriptionSerializer,
)

TAG = "Контакты"


@extend_schema(tags=[TAG], summary="FAQ")
@method_decorator(cache_page(get_cache_ttl()), name='dispatch')
class FAQListView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQListSerializer
    pagination_class = ListResultsSetPagination


@extend_schema(tags=[TAG], summary="Подписаться на рассылку")
class SubscriptionView(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


@extend_schema(tags=[TAG], summary="Футер")
@method_decorator(cache_page(get_cache_ttl()), name='dispatch')
class FooterView(BaseSectionViewMixin):
    model = Footer
    serializer_class = FooterSerializer


@extend_schema(tags=[TAG], summary="Список контактов")
@method_decorator(cache_page(get_cache_ttl()), name='dispatch')
class ContactView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


@extend_schema(tags=[TAG], summary="Отправить обратную связь")
class FeedbackView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
