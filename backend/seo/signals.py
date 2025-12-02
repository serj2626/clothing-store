from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from contacts.models import FAQ

from .models import SEO
from .service import generate_faq_json_ld


@receiver([post_save, post_delete], sender=FAQ)
def update_seo_faq_json_ld(sender, instance, **kwargs):
    """
    При добавлении/изменении/удалении FAQ обновляем seo.json_ld
    """

    seo, _ = SEO.objects.get_or_create(slug='faq')

    seo.json_ld = generate_faq_json_ld()
    seo.save(update_fields=["json_ld"])
