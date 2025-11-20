from django.contrib import admin

from .models import Review, ReviewCompanyReply, ReviewPhoto


class ReviewCompanyReplyInline(admin.TabularInline):
    model = ReviewCompanyReply
    max_num = 1
    extra = 0


class ReviewPhotoInline(admin.TabularInline):
    model = ReviewPhoto
    max_num = 5
    extra = 0


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    '''Admin View for'''

    list_display = ('user', 'product', 'rating')
    filter_horizontal = ('likes', 'dislikes')
    inlines = [ReviewCompanyReplyInline, ReviewPhotoInline]
    fields = (
        ('product', 'user'),
        ('rating', 'is_published'),
        ('advantages', 'disadvantages'),
        'likes',
        'dislikes',
        'description',
    )
