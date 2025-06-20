from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from django.conf import settings
from .serializers import RegisterSerializer, UserInfoSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

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
    pass


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
    pass


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
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
#         if response.status_code == status.HTTP_200_OK:
#             refresh = response.data.get("refresh")
#             access = response.data.get("access")
#             response.set_cookie(
#                 key="refresh_token",
#                 value=refresh,
#                 httponly=True,
#                 secure=True,
#                 samesite="Lax",
#                 path="/api/v1/users/token/refresh/",
#                 max_age=7 * 24 * 60 * 60,
#             )
#             data = {"access": access}
#             response.data = data
#         return response


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
#     def post(self, request, *args, **kwargs):
#         # Возьмем refresh токен из cookie, а не из тела
#         refresh = request.COOKIES.get("refresh_token")
#         if not refresh:
#             return Response(
#                 {"detail": "Refresh token not found."},
#                 status=status.HTTP_401_UNAUTHORIZED,
#             )

#         request.data["refresh"] = refresh
#         response = super().post(request, *args, **kwargs)

#         if response.status_code == status.HTTP_200_OK:
#             new_refresh = response.data.get("refresh")
#             new_access = response.data.get("access")
#             # Обновляем куку с новым refresh
#             response.set_cookie(
#                 key="refresh_token",
#                 value=new_refresh,
#                 httponly=True,
#                 secure=True,
#                 samesite="Lax",
#                 path="/api/v1/users/token/refresh/",
#                 max_age=7 * 24 * 60 * 60,
#             )
#             # Отдаем клиенту только access
#             response.data = {"access": new_access}
#         return response


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
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)

#         if response.status_code == 200:
#             access_token = response.data.get("access")
#             refresh_token = response.data.get("refresh")

#             # Устанавливаем cookies
#             response.set_cookie(
#                 key=settings.SIMPLE_JWT["AUTH_COOKIE"],
#                 value=access_token,
#                 expires=settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
#                 secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
#                 httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
#                 samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
#                 path=settings.SIMPLE_JWT["AUTH_COOKIE_PATH"],
#             )

#             response.set_cookie(
#                 key="refresh_token",
#                 value=refresh_token,
#                 expires=settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"],
#                 secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
#                 httponly=True,
#                 samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
#                 path="/api/auth/refresh/",
#             )

#             # Удаляем токены из тела ответа
#             del response.data["access"]
#             del response.data["refresh"]

#         return response
