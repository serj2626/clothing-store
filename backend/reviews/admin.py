from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from common.mixins import AvatarPreviewMixin

from .models import Review, ReviewCompanyReply, ReviewPhoto


class ReviewCompanyReplyInline(admin.TabularInline):
    model = ReviewCompanyReply
    max_num = 1
    extra = 0


class ReviewPhotoInline(AvatarPreviewMixin, admin.TabularInline):
    model = ReviewPhoto
    max_num = 5
    extra = 0
    image_field_name = "image"
    image_height = 30
    readonly_fields = ("avatar_preview",)
    fields = ("image", "avatar_preview")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    '''Admin View for'''

    actions = [
        "publish_reviews",
        "unpublish_reviews",
        "clear_likes",
        "clear_dislikes",
        "set_rating_five",
    ]

    list_display = (
        'user',
        'product',
        'rating',
        'is_published',
        'get_reply',
        "get_count_likes",
        "get_count_dislikes",
        'created_at',
    )
    list_filter = ('user', 'product', 'is_published', 'rating', 'created_at')
    ordering = (
        'user',
        'product',
        'rating',
    )
    list_editable = ('is_published',)
    filter_horizontal = ('likes', 'dislikes')
    inlines = [ReviewCompanyReplyInline, ReviewPhotoInline]
    readonly_fields = ('created_at',)
    fields = (
        ('product', 'user'),
        ('rating', 'is_published', 'created_at'),
        'description',
        ('advantages', 'disadvantages'),
        'likes',
        'dislikes',
    )

    def get_reply(self, obj):
        res = obj.replies.exists()
        if res:
            return mark_safe(
                f'<span style="color: green; text-transform: uppercase;font-weight: bold">ДА</span>'
            )
        return mark_safe(
            f'<span style="color: red; text-transform: uppercase;font-weight: bold">НЕТ</span>'
        )

    get_reply.short_description = 'Есть ответ?'

    @admin.action(description="Опубликовать выбранные отзывы")
    def publish_reviews(self, request, queryset):
        updated = queryset.update(is_published=True)
        self.message_user(request, f"Опубликовано: {updated} отзывов.")

    @admin.action(description="Снять с публикации выбранные отзывы")
    def unpublish_reviews(self, request, queryset):
        updated = queryset.update(is_published=False)
        self.message_user(request, f"Снято с публикации: {updated} отзывов.")

    @admin.action(description="Очистить лайки у выбранных отзывов")
    def clear_likes(self, request, queryset):
        for review in queryset:
            review.likes.clear()
        self.message_user(request, "Лайки очищены.")

    @admin.action(description="Очистить дизлайки у выбранных отзывов")
    def clear_dislikes(self, request, queryset):
        for review in queryset:
            review.dislikes.clear()
        self.message_user(request, "Дизлайки очищены.")

    @admin.action(description="Поставить рейтинг 5 выбранным отзывам")
    def set_rating_five(self, request, queryset):
        updated = queryset.update(rating=5)
        self.message_user(request, f"Обновлено: {updated} отзывов.")
