from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models
from django.urls import reverse


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Контент")
    flag = models.CharField(max_length=100)
    complexity = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(10000)],
        verbose_name="Сложность",
    )
    category = models.ForeignKey("Category", on_delete=models.PROTECT, verbose_name="Категория")
    image = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True, null=True, verbose_name="Изображение")
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True, verbose_name="Автор")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время обновления")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("task", kwargs={"task_id": self.pk})

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"
        ordering = ["complexity", "title"]


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_id": self.pk})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
