from django.urls import path

from .views import SEOView, robots_txt_view

urlpatterns = [
    path("<slug:slug>/", SEOView.as_view(), name="seo-detail"),
    path("robots.txt", robots_txt_view, name="robots_txt"),
]
