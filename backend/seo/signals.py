from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver

from contacts.models import FAQ
from products.models import Category

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


@receiver(post_save, sender=Category)
def create_seo_for_category(sender, instance, created, **kwargs):
    """Создаём SEO запись при создании категории."""
    if not created:
        return

    if instance.parent is None:
        slug_path = f"catalog/{instance.slug}"
        SEO.objects.get_or_create(
            slug=slug_path,
            defaults={
                "og_type": SEO.OGType.WEBSITE,
                "og_site_name": "Название магазина",
                "title_seo": instance.name,
                "og_title": instance.name,
                "description": f"Купить {instance.name} по выгодной цене",
                "og_description": f"Купить {instance.name} по выгодной цене",
            },
        )


# @receiver(pre_save, sender=Category)
# def update_seo_if_slug_changed(sender, instance, **kwargs):
#     """Обновить SEO, если slug категории изменён."""
#     if not instance.pk:
#         return

#     old = Category.objects.get(pk=instance.pk)

#     if old.slug != instance.slug:
#         old_slug = f"catalog/{old.slug}"
#         new_slug = f"catalog/{instance.slug}"

#         try:
#             seo = SEO.objects.get(slug=old_slug)
#             seo.slug = new_slug
#             seo.title = instance.name
#             seo.og_title = instance.name
#             seo.save()
#         except SEO.DoesNotExist:
#             pass
