from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_spectacular.utils import extend_schema
from rest_framework import generics, response, status

from common.mixins import BaseSectionViewMixin

from .models import Contact, Feedback, Footer, Subscription
from .serializers import (
    ContactSerializer,
    FeedbackSerializer,
    FooterSerializer,
    SubscriptionSerializer,
)

TAG = "Контакты"


class SubscriptionView(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    @extend_schema(tags=[TAG], summary="Подписаться на рассылку")
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            self.perform_create(serializer)
        except Exception as e:
            raise e

        return response.Response(
            {
                "msg": "Вы успешно подписались на рассылку",
                "status": "success",
            },
            status=status.HTTP_201_CREATED,
        )


@method_decorator(cache_page(60 * 10), name="get")
class FooterView(BaseSectionViewMixin):
    model = Footer
    serializer_class = FooterSerializer

    @extend_schema(tags=[TAG], summary="Футер")
    def get(self, request):
        return super().get(request)


class ContactView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    @extend_schema(tags=[TAG], summary="Список контактов")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class FeedbackView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    @extend_schema(tags=[TAG], summary="Отправить обратную связь")
    def post(self, request, *args, **kwargs):
        self.create(request, *args, **kwargs)
        return response.Response(
            {"msg": "Форма успешно отправлена", "status": "success"},
            status=status.HTTP_201_CREATED,
        )
