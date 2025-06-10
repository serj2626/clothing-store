from django.conf import settings
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from seo_config.views import robots_txt_view


urlpatterns = [
    path("robots.txt", robots_txt_view, name="robots_txt"),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    path("admin/", admin.site.urls),
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/v1/schema/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger",
    ),
    path(
        "api/v1/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("api/v1/users/", include("users.urls")),
    path("api/v1/products/", include("products.urls")),
    path("api/v1/legal/", include("legal.urls")),
    path("api/v1/contacts/", include("contacts.urls")),
    path("api/v1/orders/", include("orders.urls")),
    path("api/v1/seo/", include("seo_config.urls")),
]

if settings.DEBUG:
    # urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
