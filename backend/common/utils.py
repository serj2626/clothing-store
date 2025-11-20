from io import BytesIO

from django.core.files.base import ContentFile
from PIL import Image
from rest_framework import serializers


def get_client_ip(request):
    """
    Функция для получения IP-адреса клиента
    """
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def resize_variants(image_field):
    """
    Возвращает изображения разных размеров (ширина):
    1. Маленькое (300px)
    2. Среднее (600px)
    3. Большое (1024px)
    """

    def resize(width):
        image = Image.open(image_field)
        image = image.convert("RGB")  # обязательно для webp
        aspect_ratio = image.height / image.width
        new_height = int(width * aspect_ratio)
        resized = image.resize((width, new_height), Image.LANCZOS)
        buffer = BytesIO()
        resized.save(buffer, format="webp", quality=85)
        return ContentFile(buffer.getvalue(), name=f"image_{width}.webp")

    small = resize(300)
    medium = resize(600)
    large = resize(1024)

    return small, medium, large


class RelativeOnlyImageField(serializers.ImageField):
    """
    Поле для изображений, которое сохраняет только имя файла
    """

    def to_representation(self, value):
        if not value:
            return None
        return value.name


def get_cache_ttl(minutes: int = 5):
    return minutes * 60


class RelativeOnlyFileField(serializers.FileField):
    """
    Поле для файлов, которое возвращает относительный путь (value.name),
    без абсолютного URL
    """

    def to_representation(self, value):
        if not value:
            return None
        return value.name
