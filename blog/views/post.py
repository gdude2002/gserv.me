from django.shortcuts import render
from django.views import View

from blog.models import Post


class PostView(View):
    def get(self, request, slug: str):
        post = Post.objects.get(slug=slug)

        return render(
            request, "blog/post.html",
            context={"post": post}
        )
