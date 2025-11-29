from django.urls import path

from .views import LikeToggleAPIView

urlpatterns = [
    path("likes/toggle/", LikeToggleAPIView.as_view(), name="likes-toggle"),
]
