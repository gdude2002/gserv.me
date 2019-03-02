from django.urls import path

from blog.views.posts import PostsView
from gserv_me.views.pattern_redirect import PatternRedirectView
from .views.index import IndexView


urlpatterns = (
    path("", IndexView.as_view(), name="blog.index"),
    path("posts", PatternRedirectView.as_view(
        pattern_name="blog.posts",
        reverse_args=(1, )
    )),
    path("posts/<int:page>", PostsView.as_view(), name="blog.posts"),
)
