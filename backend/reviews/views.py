from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from common.pagination import ListResultsSetPagination
from .models import Review
from .serializers import ReviewCompanyReplySerializer, ReviewSerializer


@extend_schema(tags=['Отзывы'])
class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    pagination_class = ListResultsSetPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["rating", "created_at"]
    ordering = ["-created_at"]

    def get_queryset(self):
        qs = Review.objects.filter(is_published=True).all()

        product_id = self.request.query_params.get("product_id")
        if product_id:
            qs = qs.filter(product_id=product_id)

        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @extend_schema(
        summary="Получить список отзывов",
        description="Возвращает список всех отзывов с пагинацией.",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Создать отзыв",
        description="Создаёт отзыв от имени авторизованного пользователя.",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Получить отзыв",
        description="Возвращает детальную информацию об отзыве.",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Обновить отзыв",
        description="Полностью обновляет данные отзыва.",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Частичное обновление отзыва",
        description="Позволяет обновить часть полей отзыва.",
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Удалить отзыв",
        description="Удаляет отзыв по ID.",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @extend_schema(
        summary="Ответ на отзыв",
        request=ReviewCompanyReplySerializer,
        responses=ReviewCompanyReplySerializer,
    )
    @action(detail=True, methods=['post'])
    def reply(self, request, pk=None):
        review = self.get_object()
        serializer = ReviewCompanyReplySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user, review=review)
        return Response(serializer.data, status=201)

    @action(detail=True, methods=['post'])
    def add_like(self, request, pk=None):
        review = self.get_object()
        review.likes.add(request.user)
        return Response({"msg": "Вы поставили лайк"})

    @action(detail=True, methods=['post'])
    def add_dislike(self, request, pk=None):
        review = self.get_object()
        review.dislikes.add(request.user)
        return Response({"msg": "Вы поставили дизлайк"})

    @action(detail=True, methods=['post'])
    def remove_like(self, request, pk=None):
        review = self.get_object()
        review.likes.remove(request.user)
        return Response({"msg": "Лайк удалён"})

    @action(detail=True, methods=['post'])
    def remove_dislike(self, request, pk=None):
        review = self.get_object()
        review.dislikes.remove(request.user)
        return Response({"msg": "Дизлайк удалён"})
