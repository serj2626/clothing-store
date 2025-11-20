from django.urls import path

from .views import SEOListView, SEOView

urlpatterns = [
    path("<slug:slug>/", SEOView.as_view(), name="seo-detail"),
    path("", SEOListView.as_view(), name="seo-list"),
]
