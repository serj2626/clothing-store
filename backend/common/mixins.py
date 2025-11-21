from django.core.exceptions import MultipleObjectsReturned
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from common.upload import compress_image


class WebpImageMixin:
    """
    Миксин для сжатия изображений
    """

    image_field_name = "image"

    def save(self, *args, **kwargs):
        if hasattr(self, self.image_field_name):
            image_field = getattr(self, self.image_field_name)
            if image_field:
                image_field = compress_image(image_field)
                setattr(self, self.image_field_name, image_field)
        super().save(*args, **kwargs)


class AdminImagePreviewMixin:
    """
    Миксин для отображения изображений в админке
    """

    image_field_name = "image"

    def get_image(self, obj):
        image_field = getattr(obj, self.image_field_name, None)
        if image_field and hasattr(image_field, "url"):
            return mark_safe(
                f'<img src="{image_field.url}" style="border-radius: 50%;" width="80" height="80">'
            )
        return "Нет изображения"

    get_image.short_description = "Фото"


class AvatarPreviewMixin:
    image_field_name = "avatar"
    image_height = 60  # можно менять в подклассах

    def avatar_preview(self, obj=None):
        instance = obj if obj is not None else self
        image = getattr(instance, self.image_field_name, None)
        if image:
            return format_html(
                f'<img src="{image.url}" style="max-height: {self.image_height}px; box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);" />'
            )
        return "Нет изображения"

    avatar_preview.short_description = "Превью"


class SingletonAdminInfoMixin:
    """
    Миксин для отображения дополнительной информации в админке
    """

    singleton_info_text = "Можно создать только один экземпляр"
    singleton_info_color = "red"
    singleton_limit = 1

    def get_desc(self, obj):
        return format_html(
            '<span style="color: {};">{}</span>',
            self.singleton_info_color,
            self.singleton_info_text,
        )

    get_desc.short_description = "Доп Инфа"

    def has_add_permission(self, request):
        return self.model.objects.count() < self.singleton_limit


class AdminLimitMixin:
    """
    Миксин для ограничения количества экземпляров в админке
    """

    singleton_limit = 1

    def has_add_permission(self, request):
        return self.model.objects.count() < self.singleton_limit


class AdminShortDescriptionMixin:
    """
    Миксин для отображения короткого описания в админке
    """

    description_field_name = "description"
    description_length = 26

    def get_description(self, obj):
        value = getattr(obj, self.description_field_name, "")
        if not value:
            return "Нет описания"
        return f"{str(value)[:self.description_length]}..."

    get_description.short_description = "Описание"


class BaseSectionViewMixin(APIView):
    model = None
    serializer_class = None

    def get(self, request):
        try:
            instance = self.model.objects.get()
        except self.model.DoesNotExist:
            raise NotFound(detail=f"{self.model.__name__} not found.")
        except MultipleObjectsReturned:
            raise NotFound(
                detail=f"Multiple {self.model.__name__} objects found. Only one expected."
            )

        serializer = self.serializer_class(instance)
        return Response(serializer.data)
