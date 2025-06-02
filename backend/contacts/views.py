from rest_framework import generics, status, response

from common.mixins import BaseSectionViewMixin

from .models import Contact, Feedback, Footer
from .serializers import ContactSerializer, FeedbackSerializer, FooterSerializer
from drf_spectacular.utils import extend_schema


TAG = "Контакты"


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
