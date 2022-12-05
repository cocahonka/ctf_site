from django.contrib.auth.models import User
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from apps.cyberpolygon.models import Category

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance: User, created, **kwargs):
    if created:
        attrs_needed = ["_category"]
        if instance.is_superuser:
            profile = Profile.objects.create(user=instance, image="profiles/defaults/admin.jpg")
            profile.category.set(Category.objects.all())
        if all(hasattr(instance, attr) for attr in attrs_needed):
            profile = Profile.objects.create(user=instance)
            profile.category.set(instance._category)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


# Optional method, since you cannot delete a profile in the admin panel,
# but for security need
@receiver(post_delete, sender=Profile)
def delete_profile(sender, instance, *args, **kwargs):
    if instance.user:
        instance.user.delete()
