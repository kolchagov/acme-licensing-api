from django import forms
from django.contrib.auth.forms import AuthenticationForm

from accounts.models import User
from acme_licensing_api.forms import BootstrapForm


class LoginForm(BootstrapForm, AuthenticationForm):
    pass


class UserDetailForm(BootstrapForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "is_company", "company_name", "logo", "iban"]
        widgets = {
            "company_name": forms.TextInput(
                attrs={"placeholder": "e.g. Acme Distributors Ltd."}
            ),
            "iban": forms.TextInput(
                attrs={"placeholder": "IBAN CODE (only for distributors)"}
            ),
        }
