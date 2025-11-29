from django.db import models
from django.db.models import Avg, Count


class ProductQuerySet(models.QuerySet):
    def with_stats(self):
        return self.annotate(
            reviews_count=Count("reviews"),
            product_likes_count=Count("likes"),
            product_comments_count=Count("comments"),
            rating_avg=Avg("reviews__rating"),
        )


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def with_stats(self):
        return self.get_queryset().with_stats()
