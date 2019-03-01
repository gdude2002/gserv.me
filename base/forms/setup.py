from crispy_forms.helper import FormHelper
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from django.forms import Form, CharField, PasswordInput
# from django_crispy_bulma.forms import EmailField

from django_crispy_bulma.layout import Submit


class SetupForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.add_input(Submit("submit", "Submit", css_class="is-fullwidth"))

    username = CharField(
        label="Username",
        max_length=150,
        required=True,
        validators=(UnicodeUsernameValidator(), ),
    )

    # email = EmailField(
    #     label="Email",
    #     required=True,
    # )

    password = CharField(
        label="Password",
        required=True,
        widget=PasswordInput,
    )

    confirm_password = CharField(
        label="Password (Again)",
        required=True,
        widget=PasswordInput,
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        print(password, confirm_password)
        print(password == confirm_password)

        if password != confirm_password:
            self.add_error("password", ValidationError("Passwords must match"))
            self.add_error("confirm_password", ValidationError("Passwords must match"))

    def _post_clean(self):
        del self.cleaned_data["confirm_password"]
