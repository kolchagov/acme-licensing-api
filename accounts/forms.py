from django import forms

from accounts.models import AccountDetail


class AccountDetailForm(forms.ModelForm):
    class Meta:
        model = AccountDetail
        fields = ["user", "company_name", "logo", "iban"]
        widgets = {
            "company_name": forms.TextInput(
                attrs={"placeholder": "e.g. Acme Licensing Ltd. (optional)"}
            ),
            "iban": forms.TextInput(
                attrs={"placeholder": "IBAN CODE (optional)"}
            ),
        }
