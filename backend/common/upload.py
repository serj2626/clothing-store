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


# @deconstructible
# class CustomStorage(FileSystemStorage):
#     """
#     Кастомное хранилище для CKEditor5.
#     Загруженные файлы будут сохраняться в /media/uploads/ckeditor/YYYY/MM/DD/
#     и доступны по URL /media/uploads/ckeditor/...
#     """

#     def __init__(self, location=None, base_url=None):
#         # Папка, куда сохраняются файлы
#         location = location or os.path.join(
#             settings.MEDIA_ROOT, "uploads/ckeditor"
#         )
#         base_url = base_url or f"{settings.MEDIA_URL}uploads/ckeditor/"
#         super().__init__(location, base_url)

#     def get_available_name(self, name, max_length=None):
#         """
#         Если файл с таким именем уже есть — добавляем уникальный суффикс.
#         """
#         if self.exists(name):
#             base, ext = os.path.splitext(name)
#             name = f"{base}_{datetime.now().strftime('%Y%m%d%H%M%S')}{ext}"
#         return name

#     def _save(self, name, content):
#         """
#         При сохранении создаем поддиректорию по дате: /YYYY/MM/DD/
#         """
#         date_path = datetime.now().strftime("%Y/%m/%d")
#         name = os.path.join(date_path, name)
#         return super()._save(name, content)
