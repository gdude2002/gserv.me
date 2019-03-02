from django.urls import path, include
from django.views.generic import TemplateView

from .views.setup.index import IndexView as SetupIndexView


urlpatterns = (
    path("", TemplateView.as_view(template_name="base/index.html"), name="base.index"),
    path('accounts/', include('django.contrib.auth.urls')),
    path("setup/", SetupIndexView.as_view(), name="base.setup"),
)
