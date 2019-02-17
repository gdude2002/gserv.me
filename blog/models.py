from django.contrib.auth.models import User
from django.db import models

from blog.constants import BlockType


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    html = models.TextField()
    slug = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.title


class Block(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    type = models.IntegerField(
        choices=[(t, t.value) for t in BlockType]
    )
    content = models.TextField()
    order = models.IntegerField()
