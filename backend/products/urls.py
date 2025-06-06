from django.urls import path

# from .views import create_checkout_session
from .views import (
    CategoryDetailView,
    ProductListView,
    ProductDetailView,
    toggle_product_like,
    CategoryListView,
    BrandListView,
)

urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    path("<uuid:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("<uuid:product_id>/like/", toggle_product_like, name="product_like"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path(
        "categories/<slug:slug>/", CategoryDetailView.as_view(), name="category-detail"
    ),
    path("brands/", BrandListView.as_view(), name="brand-list"),
    # path('api/checkout/', create_checkout_session, name='create_checkout'),
]
