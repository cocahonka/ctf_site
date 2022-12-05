from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import m2m_changed
from django.urls import reverse

from apps.cyberpolygon.models import Category


def profile_upload_to(instance, filename):
    return f"profiles/{instance.user.username}/{filename}"


def regions_changed(sender, **kwargs):
    if not kwargs["instance"].user.is_superuser:
        if kwargs["instance"].category.count() > 3:
            raise ValidationError("Нелья выбрать больше 3 категорий")


# TODO add student card field
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    image = models.ImageField(
        default="profiles/defaults/user.jpg", upload_to=profile_upload_to, verbose_name="Аватарка"
    )
    category = models.ManyToManyField(Category, verbose_name="Категории")
    is_verified = models.BooleanField(default=False, verbose_name="Верефецирован")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("profile_id", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профиля"


m2m_changed.connect(regions_changed, sender=Profile.category.through)
