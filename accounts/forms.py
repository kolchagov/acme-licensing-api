from django import forms

from accounts.models import User


class UserDetailForm(forms.ModelForm):
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
