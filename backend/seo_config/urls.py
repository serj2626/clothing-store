from django.urls import path

from .views import SEOView

urlpatterns = [
    path("<slug:slug>/", SEOView.as_view(), name="seo-detail"),
]
