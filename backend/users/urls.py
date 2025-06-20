from django.urls import path
from .views import (
    LogoutView,
    RegisterView,
    UserDetailView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", CustomTokenRefreshView.as_view(), name="token_refresh"),
    path("detail/info/", UserDetailView.as_view(), name="user-detail"),
    path("api/auth/logout/", LogoutView.as_view(), name="logout"),
]
