from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Category


@receiver(post_save, sender=Category)
def update_admin_categories(sender, instance: Category, created, **kwargs):
    if created:
        super_users = User.objects.filter(is_superuser=True)
        for user in super_users:
            user.profile.category.add(instance)
