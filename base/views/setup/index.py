from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from base.forms.setup import SetupForm


INDEX_URL = "base.index"

SETUP_DONE_TEMPLATE = "base/setup_done.html"
SETUP_TEMPLATE = "base/setup.html"


class IndexView(View):
    def get(self, request):
        users = User.objects.filter(is_superuser=True).count()

        if users > 0:
            return redirect(INDEX_URL)

        return render(
            request, SETUP_TEMPLATE,
            context={
                "setup_form": SetupForm()
            }
        )

    def post(self, request: HttpRequest):
        users = User.objects.filter(is_superuser=True).count()

        if users > 0:
            return redirect(INDEX_URL)

        form = SetupForm(request.POST)

        if not form.is_valid():
            return render(
                request, SETUP_TEMPLATE,
                context={
                    "setup_form": form
                }
            )

        user = User.objects.create_superuser(**form.cleaned_data)
        user.save()

        return render(
            request, SETUP_DONE_TEMPLATE
        )
