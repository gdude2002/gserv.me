from django.db.models import Count
from django.shortcuts import render
from django.views import View

from blog.models import Category


class CategoriesView(View):
    def get(self, request):
        categories = Category.objects.order_by("name").annotate(post_count=Count("post"))

        return render(
            request, "blog/categories.html",
            context={"categories": categories}
        )
