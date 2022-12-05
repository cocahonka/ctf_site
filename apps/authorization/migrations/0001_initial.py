# Generated by Django 4.1.3 on 2022-12-05 14:34

import apps.authorization.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cyberpolygon", "0002_alter_task_attached_file"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        default="profiles/defaults/user.jpg",
                        upload_to=apps.authorization.models.profile_avatar_upload_to,
                        verbose_name="Аватарка",
                    ),
                ),
                (
                    "is_verified",
                    models.BooleanField(default=False, verbose_name="Верефецирован"),
                ),
                (
                    "student_card",
                    models.ImageField(
                        upload_to=apps.authorization.models.profile_student_card_upload_to,
                        verbose_name="Студенческий  билет",
                    ),
                ),
                (
                    "category",
                    models.ManyToManyField(
                        to="cyberpolygon.category", verbose_name="Категории"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Профиль",
                "verbose_name_plural": "Профиля",
            },
        ),
    ]
