from django.urls import path, include
from django.views.generic import TemplateView

from . import views


urlpatterns = (
    path("", TemplateView.as_view(template_name="base/index.html"), name="base.index"),
    path('accounts/', include('django.contrib.auth.urls')),
    path("setup/", views.SetupIndexView.as_view(), name="base.setup"),
)
