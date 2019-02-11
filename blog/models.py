from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    markdown = models.TextField()
    html = models.TextField()
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=1024)
    username = models.CharField(max_length=64)

    def __str__(self):
        return f"@{self.username} | {self.text}"
