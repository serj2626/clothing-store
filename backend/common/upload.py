from io import BytesIO

from django.core.files.base import ContentFile
from PIL import Image


def compress_image(image_field, quality=90):
    """
    Компрессия изображения
    """
    # Открываем изображение через Pillow
    image = Image.open(image_field)

    # Создаём временный буфер для хранения обработанного изображения
    buffer = BytesIO()

    # Сохраняем изображение в буфер в формате webp с качеством 90%
    image.save(buffer, format="webp", quality=quality)

    # Перезаписываем поле изображения новым сжатым содержимым
    image_field.save("image.webp", ContentFile(buffer.getvalue()), save=False)

    # Возвращаем поле
    return image_field
