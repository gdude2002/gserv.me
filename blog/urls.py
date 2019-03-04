from django.urls import path

from blog.views.categories import CategoriesView
from blog.views.category import CategoryView
from blog.views.post import PostView
from blog.views.posts import PostsView
from gserv_me.views.pattern_redirect import PatternRedirectView


urlpatterns = (
    # Redirects
    path("", PatternRedirectView.as_view(  # Index view
        pattern_name="blog.posts",
        reverse_kwargs={"page": 1}
    ), name="blog.index"),
    path("posts", PatternRedirectView.as_view(  # Posts index
        pattern_name="blog.posts",
        reverse_kwargs={"page": 1}
    )),
    path("p", PatternRedirectView.as_view(  # Post without a slug
        pattern_name="blog.posts",
        reverse_kwargs={"page": 1}
    )),

    # Actual views
    path("posts/<int:page>", PostsView.as_view(), name="blog.posts"),
    path("p/<slug:slug>", PostView.as_view(), name="blog.post"),
    path("categories", CategoriesView.as_view(), name="blog.categories"),
    path("c/<slug:slug>/<int:page>", CategoryView.as_view(), name="blog.category"),
)
