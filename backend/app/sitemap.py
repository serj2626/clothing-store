from django.contrib.sitemaps import Sitemap
from products.models import Product, Category
from seo_config.models import SEO


class SEOSitemap(Sitemap):
    def items(self):
        return SEO.objects.all()

    def location(self, obj):
        return f"/{obj.slug}"

    def lastmod(self, obj):
        return obj.lastmod

    def changefreq(self, obj):
        return obj.changefreq

    def priority(self, obj):
        return obj.priority


class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Product.objects.all()

    def location(self, obj):
        return f"/products/{obj.id}/"

    def lastmod(self, obj):
        return obj.updated_at


class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Category.objects.all()

    def location(self, obj):
        return f"/categories/{obj.slug}/"
