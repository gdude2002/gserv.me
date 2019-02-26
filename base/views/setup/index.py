from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from base.forms.setup import SetupForm


class IndexView(View):
    def get(self, request):
        users = User.objects.filter(is_staff=True).count()

        if users > 0:
            return redirect("base.index")

        return render(request, "base/setup.html", context={"setup_form": SetupForm()})

    def post(self, request: HttpRequest):
        users = User.objects.filter(is_staff=True).count()

        if users > 0:
            return redirect("base.index")

        form = SetupForm(request.POST)

        if not form.is_valid():
            return render(
                request, "base/setup.html",
                context={
                    "setup_form": form
                }
            )

        data = form.cleaned_data

        user = User.objects.create_superuser(
            data["username"], data["email"], data["password"]
        )

        user.save()

        return render(request, "base/setup_done.html")
