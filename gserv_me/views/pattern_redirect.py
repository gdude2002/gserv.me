from django.urls import reverse
from django.views.generic import RedirectView


class PatternRedirectView(RedirectView):
    reverse_args = None
    reverse_kwargs = None

    def get_redirect_url(self, *args, **kwargs):
        """
        Return the URL to redirect to, similarly to Django's own RedirectView.
        Additionally, if using `pattern_name`, then providing `args` or `kwargs`
        will pass those values along to `reverse()`.
        """
        if (self.reverse_args or self.reverse_kwargs) and self.pattern_name:
            if self.reverse_args:
                url = reverse(
                    self.pattern_name,

                    args=self.reverse_args
                )
            else:
                url = reverse(
                    self.pattern_name,
                    kwargs=self.reverse_kwargs
                )

            query = self.request.META.get("QUERY_STRING", "")

            if query and self.query_string:
                url = f"{url}?{query}"

            return url

        return super().get_redirect_url(*args, **kwargs)


