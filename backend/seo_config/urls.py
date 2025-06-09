from django.urls import path

from .views import SEOView, robots_txt_view

from django.urls import path, re_path
from django.contrib.sitemaps.views import sitemap

# from configs.views import robots_txt, StaticSitemap, PortfolioSitemap, SpecialistSitemap, SubServiceSitemap, \
#     ServiceSitemap, SEOAPIView, BlogSitemap

# app_name = "seo_configs"

# sitemaps = {
#     "static": StaticSitemap,
#     "portfolio": PortfolioSitemap,
#     "specialist": SpecialistSitemap,
#     "sub_service": SubServiceSitemap,
#     "services": ServiceSitemap,
#     "blog": BlogSitemap,
# }


urlpatterns = [
    path("<slug:slug>/", SEOView.as_view(), name="seo-detail"),
    path("robots.txt", robots_txt_view, name="robots_txt"),
]
