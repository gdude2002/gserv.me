from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from blog.models import Post


class PostsView(View):
    def get(self, request, page: int):
        posts = Post.objects.order_by("-pub_date")
        pages = Paginator(posts, per_page=10)

        return render(
            request, "blog/index.html",
            context={"posts": pages.get_page(page)}
        )
