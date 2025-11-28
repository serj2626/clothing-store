from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from orders.models import Cart

from .models import Profile, User


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        # if created:
        Profile.objects.get_or_create(user=instance)
        Cart.objects.create(user=instance)
    else:
        instance.profile.save()


@receiver(post_delete, sender=User)
def delete_profile(sender, instance, **kwargs):
    try:
        instance.profile.delete()
    except Profile.DoesNotExist:
        pass
