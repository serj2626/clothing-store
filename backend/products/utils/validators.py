from django.core.exceptions import ValidationError
from PIL import Image


def validate_file_size(image):
    max_size = 2 * 1024 * 1024  # 2 MB
    if image.size > max_size:
        raise ValidationError("Размер файла не должен превышать 2 MB")


def validate_image_size(image):
    img = Image.open(image)
    max_width, max_height = 1024, 1024
    if img.width > max_width or img.height > max_height:
        raise ValidationError(
            f"Размер изображения не должен превышать {max_width}x{max_height}"
        )
