from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from blog.models import Post


class IndexView(View):
    def get(self, request):
        posts = Post.objects.order_by("-pub_date")  # Latest 10 posts
        pages = Paginator(posts, per_page=10)

        return render(
            request, "blog/index.html",
            context={"posts": pages.get_page(1)}
        )
