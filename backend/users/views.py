from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .serializers import RegisterSerializer, UserInfoSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework.permissions import IsAuthenticated

TAG = "Аутентификация и Пользователи"


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


# @extend_schema(
#     tags=[TAG],
#     summary="Получение JWT токена",
#     description="Возвращает access и refresh токены по email и паролю.",
#     responses={
#         200: OpenApiResponse(
#             response={"access": "string", "refresh": "string"},
#             description="Успешная аутентификация",
#         )
#     },
# )
# class CustomTokenObtainPairView(TokenObtainPairView):
#     pass


# @extend_schema(
#     tags=[TAG],
#     summary="Обновление JWT токена",
#     description="Обновляет access токен по действующему refresh токену.",
#     responses={
#         200: OpenApiResponse(
#             response={"access": "string"}, description="Новый access токен"
#         )
#     },
# )
# class CustomTokenRefreshView(TokenRefreshView):
#     pass


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
        if response.status_code == status.HTTP_200_OK:
            refresh = response.data.get("refresh")
            access = response.data.get("access")
            # Кладем refresh в куку
            response.set_cookie(
                key="refresh_token",
                value=refresh,
                httponly=True,
                secure=True,
                samesite="Lax",
                path="/api/v1/users/token/refresh/",
                max_age=7 * 24 * 60 * 60,
            )
            # Удаляем refresh из тела, чтобы клиент не видел
            data = {"access": access}
            response.data = data
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
        # Возьмем refresh токен из cookie, а не из тела
        refresh = request.COOKIES.get("refresh_token")
        if not refresh:
            return Response(
                {"detail": "Refresh token not found."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        request.data["refresh"] = refresh
        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            new_refresh = response.data.get("refresh")
            new_access = response.data.get("access")
            # Обновляем куку с новым refresh
            response.set_cookie(
                key="refresh_token",
                value=new_refresh,
                httponly=True,
                secure=True,
                samesite="Lax",
                path="/api/v1/users/token/refresh/",
                max_age=7 * 24 * 60 * 60,
            )
            # Отдаем клиенту только access
            response.data = {"access": new_access}
        return response
