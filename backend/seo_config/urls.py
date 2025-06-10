from django.urls import path

from .views import SEODetailView, sitemap_xml, SEOListView

from django.urls import path

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
    path("", SEOListView.as_view(), name="seo_list"),
    path("<slug:slug>/", SEODetailView.as_view(), name="seo_detail"),
    path("sitemap.xml", sitemap_xml, name="sitemap-xml"),
]
