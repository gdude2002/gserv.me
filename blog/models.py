from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    html = models.TextField()
    markdown = models.TextField()
    slug = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.title
