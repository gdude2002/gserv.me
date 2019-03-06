from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render
from django.views import View

from blog.models import Category


class CategoryView(View):
    def get(self, request, slug: str, page: int):
        category = Category.objects.annotate(post_count=Count("post")).get(slug=slug)
        pages = Paginator(category.post_set.order_by("-pub_date").all(), per_page=10)

        return render(
            request, "blog/index.html",
            context={"posts": pages.get_page(page), "category": category}
        )
