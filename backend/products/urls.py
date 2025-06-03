from django.urls import path
# from .views import create_checkout_session
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    path("<uuid:pk>/", ProductDetailView.as_view(), name="product-detail"),
    # path('api/checkout/', create_checkout_session, name='create_checkout'),
]