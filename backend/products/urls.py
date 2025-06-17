from django.urls import path

# from .views import create_checkout_session
from .views import (
    CategoryDetailView,
    ProductLastCollectionView,
    ProductListView,
    ProductDetailView,
    toggle_product_like,
    list_comments_by_product,
    CategoryListView,
    BrandListView,
    ReviewCreateView,
    ProductExampleListView,
)

urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    path("example/", ProductListView.as_view(), name="product-list"),
    path(
        "last-collection/",
        ProductLastCollectionView.as_view(),
        name="product-last-list",
    ),
    path("<uuid:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path(
        "<uuid:product_id>/reviews/list",
        list_comments_by_product,
        name="product_detail_list_reviews",
    ),
    path(
        "<uuid:pk>/create-review",
        ReviewCreateView.as_view(),
        name="product_detail_create_review",
    ),
    path("<uuid:product_id>/like/", toggle_product_like, name="product_like"),
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path(
        "categories/<slug:slug>/", CategoryDetailView.as_view(), name="category_detail"
    ),
    path("brands/", BrandListView.as_view(), name="brand_list"),
    # path('api/checkout/', create_checkout_session, name='create_checkout'),
]
