from django.urls import path, include

from . import views


urlpatterns = (
    path("", views.IndexView.as_view(), name="base.index"),
    path('accounts/', include('django.contrib.auth.urls')),
    path("setup", views.SetupIndexView.as_view(), name="base.setup"),
)
