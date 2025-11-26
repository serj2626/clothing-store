from django.urls import path
from .views import (
    BrandListView,
    CategoryDetailView,
    CategoryListBySlugView,
    CategoryListView,
    ProductDetailView,
    ProductLastCollectionView,
    ProductListView,
    toggle_product_like,
)

urlpatterns = [
    path("<slug:slug>/list", ProductListView.as_view(), name="product-list"),
    path("example/", ProductListView.as_view(), name="product-list"),
    path(
        "last-collection/",
        ProductLastCollectionView.as_view(),
        name="product-last-list",
    ),
    path("<uuid:pk>/", ProductDetailView.as_view(), name="product-detail"),
    # path(
    #     "<uuid:product_id>/reviews/list",
    #     ReviewsListByProductView.as_view(),
    #     name="product_detail_list_reviews",
    # ),
    # path(
    #     "<uuid:pk>/create-review",
    #     ReviewCreateView.as_view(),
    #     name="product_detail_create_review",
    # ),
    path("<uuid:product_id>/like/", toggle_product_like, name="product-like"),
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
    # path('api/checkout/', create_checkout_session, name='create_checkout'),
]
