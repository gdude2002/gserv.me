from django.urls import path

from . import views


urlpatterns = (
    path("", views.IndexView.as_view(), name="base.index"),
    path("setup", views.SetupIndexView.as_view(), name="base.setup"),
)
