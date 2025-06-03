from django.urls import path

# from .views import create_checkout_session
from .views import ProductListView, ProductDetailView, toggle_product_like

urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    path("<uuid:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("products/<uuid:product_id>/like/", toggle_product_like, name="product_like"),
    # path('api/checkout/', create_checkout_session, name='create_checkout'),
]
