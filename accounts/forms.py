from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User
from acme_licensing_api.forms import BootstrapForm

UserModel = get_user_model()


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


class CustomRegistrationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'first_name', 'last_name', 'is_company', 'company_name', 'iban')

    def save(self, commit=True):
        # clean the data and save the user
        self.cleaned_data['username'] = self.cleaned_data['username'].lower()
        return super().save(commit=commit)
