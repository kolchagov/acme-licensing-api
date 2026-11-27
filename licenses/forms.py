from django import forms

from acme_licensing_api.forms import BootstrapForm
from licenses.models import License


class LicenseForm(BootstrapForm, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            # the license key is derived from the trial, make it RO
            self.fields["trial"].disabled = True

    class Meta:
        model = License
        fields = ["trial", "customer", "version", "expiry_date"]
        labels = {
            "version": "Licensed version",
            "expiry_date": "Expiry date",
        }
        widgets = {
            "version": forms.TextInput(attrs={"placeholder": "e.g. 1.2.3"}),
            "expiry_date": forms.DateInput(attrs={"type": "date"}),
        }
        error_messages = {
            "trial": {"required": "Trial record is required."},
            "customer": {"required": "Customer is required."},
            "version": {"required": "Licensed version is required."},
        }
