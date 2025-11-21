from .serializers import (
    ReviewSerializer,
    ReviewCompanyReplySerializer,
    ReviewPhotoSerializer,
)
from drf_spectacular.utils import extend_schema
from .models import Review, ReviewCompanyReply, ReviewPhoto
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action


class ReviewPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response(
            {
                'count': self.page.paginator.count,
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
                'results': data,
            }
        )


@extend_schema(tags=['Отзывы'])
class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.filter(is_published=True).order_by('-created_at')
    serializer_class = ReviewSerializer
    pagination_class = ReviewPagination
    # permission_classes = [IsAuthenticated]

    # ==========
    # BASE METHODS
    # ==========

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

    # ==========
    # ACTIONS
    # ==========
    @extend_schema(
        summary="Ответ на отзыв",
        description="Позволяет авторизованному пользователю оставить ответ на определённый отзыв.",
        request=ReviewCompanyReplySerializer,
        responses=ReviewCompanyReplySerializer,
    )
    @action(detail=True, methods=['post'])
    def reply(self, request, pk=None):
        review = self.get_object()
        serializer = ReviewCompanyReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, review=review)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        summary="Поставить лайк",
        description="Добавляет лайк к отзыву от имени текущего пользователя.",
        responses={200: dict},
    )
    @action(detail=True, methods=['post'])
    def add_like(self, request, pk=None):
        review = self.get_object()
        review.likes.add(request.user)
        return Response(
            status=status.HTTP_200_OK, data={'msg': 'Вы поставили лайк'}
        )

    @extend_schema(
        summary="Поставить дизлайк",
        description="Добавляет дизлайк к отзыву от имени текущего пользователя.",
        responses={200: dict},
    )
    @action(detail=True, methods=['post'])
    def add_dislike(self, request, pk=None):
        review = self.get_object()
        review.dislikes.add(request.user)
        return Response(
            status=status.HTTP_200_OK, data={'msg': 'Вы поставили дизлайк'}
        )

    @extend_schema(
        summary="Убрать лайк",
        description="Удаляет лайк пользователя с отзыва.",
        responses={200: dict},
    )
    @action(detail=True, methods=['post'])
    def remove_like(self, request, pk=None):
        review = self.get_object()
        review.likes.remove(request.user)
        return Response(
            status=status.HTTP_200_OK, data={'msg': 'Вы удалили лайк'}
        )

    @extend_schema(
        summary="Убрать дизлайк",
        description="Удаляет дизлайк пользователя с отзыва.",
        responses={200: dict},
    )
    @action(detail=True, methods=['post'])
    def remove_dislike(self, request, pk=None):
        review = self.get_object()
        review.dislikes.remove(request.user)
        return Response(
            status=status.HTTP_200_OK, data={'msg': 'Вы удалили дизлайк'}
        )
