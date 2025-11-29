from django.contrib.contenttypes.models import ContentType

from interactions.models import Like


def toggle_like(user, obj) -> bool:
    """
    Переключает лайк для пользователя на объекте obj.
    Возвращает True, если лайк добавлен, False если удалён.
    """
    ct = ContentType.objects.get_for_model(obj)

    like, created = Like.objects.get_or_create(
        user=user, content_type=ct, object_id=obj.id
    )

    if not created:
        like.delete()
        return False

    return True
