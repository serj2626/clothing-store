from django.urls import path

from .views import (
    BrandListView,
    CategoryDetailView,
    CategoryListBySlugView,
    CategoryListView,
    ProductDetailView,
    ProductLastCollectionView,
    ProductListView,
)

urlpatterns = [
    path("<slug:slug>/list", ProductListView.as_view(), name="product-list"),
    path(
        "last-collection/",
        ProductLastCollectionView.as_view(),
        name="product-last-list",
    ),
    path("<uuid:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path(
        "categories/<slug:slug>/list",
        CategoryListBySlugView.as_view(),
        name="category-list-by-slug",
    ),
    path(
        "categories/<slug:slug>/",
        CategoryDetailView.as_view(),
        name="category-detail",
    ),
    path("brands/", BrandListView.as_view(), name="brand-list"),
]
