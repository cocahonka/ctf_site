from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models
from django.urls import reverse


def task_upload_to(instance, filename):
    return "tasks/{0}/{1}/{2}".format(
        instance.category.slug,
        instance.pk,
        filename,
    )


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(verbose_name="Контент")
    flag = models.CharField(max_length=100)
    complexity = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(10000)],
        verbose_name="Сложность",
    )
    category = models.ForeignKey("Category", on_delete=models.PROTECT, verbose_name="Категория")
    image = models.ImageField(upload_to=task_upload_to, blank=True, null=True, verbose_name="Изображение")
    attached_file = models.FileField(upload_to=task_upload_to, verbose_name="Файл к заданию")
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True, verbose_name="Автор")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время обновления")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("task", kwargs={"task_slug": self.slug})

    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_image = self.image
            saved_attached_file = self.attached_file
            self.image = None
            self.attached_file = None
            super(Task, self).save(*args, **kwargs)
            self.image = saved_image
            self.attached_file = saved_attached_file

        super(Task, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"
        ordering = ["complexity", "title"]


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_slug": self.slug})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
