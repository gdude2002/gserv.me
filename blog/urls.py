from django.urls import path

from blog.views.post import PostView
from blog.views.posts import PostsView
from gserv_me.views.pattern_redirect import PatternRedirectView


urlpatterns = (
    path("", PatternRedirectView.as_view(
        pattern_name="blog.posts",
        reverse_kwargs={"page": 1}
    ), name="blog.index"),
    path("posts", PatternRedirectView.as_view(
        pattern_name="blog.posts",
        reverse_kwargs={"page": 1}
    )),
    path("posts/<int:page>", PostsView.as_view(), name="blog.posts"),
    path("<slug:slug>", PostView.as_view(), name="blog.post"),
)
