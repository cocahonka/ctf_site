from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


def profile_upload_to(instance, filename):
    return f"profiles/{instance.pk}/{filename}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    image = models.ImageField(default="default.png", upload_to=profile_upload_to, verbose_name="Аватарка")

    def __str__(self):
        return f"Пользователь {self.user.username}"

    def get_absolute_url(self):
        return reverse("profile_id", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профиля"
