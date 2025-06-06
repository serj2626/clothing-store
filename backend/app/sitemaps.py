from django.contrib.sitemaps import Sitemap
from django.urls import reverse
# from .models import Review


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "monthly"

    def items(self):
        return ["home", "about", "contact"]  # имена ваших URL-имен

    def location(self, item):
        return reverse(item)


# class ReviewSitemap(Sitemap):
#     changefreq = "weekly"
#     priority = 0.7

#     def items(self):
#         return Review.objects.filter(published=True)

#     def lastmod(self, obj):
#         return obj.updated_at  # или obj.created_at

#     def location(self, obj):
#         return f"/reviews/{obj.slug}/"
