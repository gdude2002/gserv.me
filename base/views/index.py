from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View


class IndexView(View):
    def get(self, request):
        users = User.objects.filter(is_staff=True).count()

        if users <= 0:
            return redirect("base.setup")

        return render(request, "base/index.html")
