from django import forms

from acme_licensing_api.forms import BootstrapForm
from licenses.models import License


class LicenseForm(BootstrapForm, forms.ModelForm):
    class Meta:
        model = License
        fields = ["trial", "customer", "version", "expiry_date"]
        widgets = {
            "expiry_date": forms.DateInput(attrs={"type": "date"}),
        }
