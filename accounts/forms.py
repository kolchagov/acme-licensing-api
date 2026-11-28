from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User
from acme_licensing_api.forms import BootstrapForm

UserModel = get_user_model()


class LoginForm(BootstrapForm, AuthenticationForm):
    pass


class RegisterForm(BootstrapForm, UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs["placeholder"] = "At least 8 characters"
        self.fields["password2"].widget.attrs["placeholder"] = "Repeat the password"
        self.order_fields([
            "username",
            "password1",
            "password2",
            'email',
            "first_name",
            'last_name',
            'is_company',
            'company_name',
            "logo",
            'iban'
        ])

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('username', 'email', 'first_name', 'last_name', 'is_company', 'company_name', "logo", 'iban')
        widgets = {
            "username": forms.TextInput(
                attrs={"placeholder": "topuser"}
            ),
            "email": forms.EmailInput(
                attrs={"placeholder": "j.doe@company.bg"}
            ),
            "first_name": forms.TextInput(
                attrs={"placeholder": "Ivan"}
            ),
            "last_name": forms.TextInput(
                attrs={"placeholder": "Petrov"}
            ),
            "company_name": forms.TextInput(
                attrs={"placeholder": "Acme Distributors Ltd."}
            ),
            "iban": forms.TextInput(
                attrs={"placeholder": "BG00ABCD1234567890"}
            ),
        }
        help_texts = {
            "username": "Used to log in. Letters only.",
            "email": "Used for password restore and notifications.",
            "is_company": "Check if this account represents a distributor.",
            "company_name": "Legal name of the company, required for distributors.",
            "iban": "IBAN CODE (only for distributors)",
            "logo": "Optional company logo.",
        }


class UserDetailForm(BootstrapForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "is_company", "company_name", "logo", "iban"]


class CustomRegistrationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'first_name', 'last_name', 'is_company', 'company_name', 'iban')

    def save(self, commit=True):
        # clean the data and save the user
        self.cleaned_data['username'] = self.cleaned_data['username'].lower()
        return super().save(commit=commit)
