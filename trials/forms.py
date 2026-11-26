from django import forms

from acme_licensing_api.forms import BootstrapForm
from trials.models import Trial


class TrialForm(BootstrapForm, forms.ModelForm):
    class Meta:
        model = Trial
        fields = ["device_sn", "app", "details"]
        widgets = {
            "details": forms.Textarea(attrs={"rows": 3}),
        }
