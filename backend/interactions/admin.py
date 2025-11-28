from django.contrib import admin

from .models import Comment, Like, Review, ReviewPhoto

admin.site.register(Like)
admin.site.register(Review)
admin.site.register(ReviewPhoto)
admin.site.register(Comment)
