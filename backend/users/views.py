from django.conf import settings
from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import generics, status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .serializers import RegisterSerializer, UserInfoSerializer

TAG = "Аутентификация и Пользователи"


class LogoutView(APIView):
    @extend_schema(tags=[TAG], summary="Выход из системы")
    def post(self, request):
        response = Response(
            {"detail": "Successfully logged out."}, status=status.HTTP_200_OK
        )
        response.delete_cookie(settings.SIMPLE_JWT["AUTH_COOKIE"])
        response.delete_cookie("refresh_token")
        return response


class UserDetailView(RetrieveAPIView):
    serializer_class = UserInfoSerializer
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=[TAG], summary="Текущий пользователь")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_object(self):
        return self.request.user


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    @extend_schema(tags=[TAG], summary="Регистрация пользователя")
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"msg": "Пользователь успешно зарегистрирован", "status": "success"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    tags=[TAG],
    summary="Получение JWT токена",
    description="Возвращает access и refresh токены по email и паролю.",
    responses={
        200: OpenApiResponse(
            response={"access": "string", "refresh": "string"},
            description="Успешная аутентификация",
        )
    },
)
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        refresh = response.data.get("refresh")
        access = response.data.get("access")

        response.data = {"msg": "Авторизация прошла успешно"}

        response.set_cookie(
            key=settings.SIMPLE_JWT["AUTH_COOKIE"],
            value=access,
            httponly=True,
            secure=False,  # True на проде
            samesite="Lax",
            path="/",
        )

        response.set_cookie(
            key="refresh_token_store",
            value=refresh,
            httponly=True,
            secure=False,
            samesite="Lax",
            path="/",
        )
        return response


@extend_schema(
    tags=[TAG],
    summary="Обновление JWT токена",
    description="Обновляет access токен по действующему refresh токену.",
    responses={
        200: OpenApiResponse(
            response={"access": "string"}, description="Новый access токен"
        )
    },
)
class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        access = response.data.get("access")
        response.data = {"detail": "Токен обновлён"}

        response.set_cookie(
            key=settings.SIMPLE_JWT["AUTH_COOKIE"],
            value=access,
            httponly=True,
            secure=False,
            samesite="Lax",
            path="/",
        )

        return response
