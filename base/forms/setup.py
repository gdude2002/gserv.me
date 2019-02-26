from crispy_forms.helper import FormHelper
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.forms import Form, CharField, PasswordInput
from django_crispy_bulma.forms import EmailField

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
        validators=(UnicodeUsernameValidator(), )
    )

    email = EmailField(
        label="Email",
        required=True,
    )

    password = CharField(
        label="Password",
        required=True,
        widget=PasswordInput,
    )
