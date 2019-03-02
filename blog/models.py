from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ("name", )

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, verbose_name="Category", on_delete=models.DO_NOTHING,
        null=True
    )

    html = models.TextField("HTML")
    markdown = models.TextField()
    slug = models.SlugField(max_length=200)
    title = models.CharField(max_length=200)

    pub_date = models.DateTimeField("date published", default=timezone.now)

    def __str__(self):
        return self.title
