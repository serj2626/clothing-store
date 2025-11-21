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

    list_display = (
        'user',
        'product',
        'rating',
        'is_published',
        "get_count_likes",
        "get_count_dislikes",
    )

    list_editable = ('is_published',)
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

    # def get_count_likes(self, obj):
    #     return obj.likes.count()

    # def get_count_dislikes(self, obj):
    #     return obj.dislikes.count()

    # get_count_likes.short_description = 'Лайки'
    # get_count_dislikes.short_description = 'Дизлайки'
