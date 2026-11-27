from django import forms

from acme_licensing_api.forms import BootstrapForm
from trials.models import Trial


class TrialForm(BootstrapForm, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            # device serial number is trial identity, make it RO
            self.fields["device_sn"].disabled = True
            if hasattr(self.instance, "license"):
                # after creation, app code is RO
                self.fields["app"].disabled = True

    class Meta:
        model = Trial
        fields = ["device_sn", "app", "details"]
        labels = {
            "device_sn": "Device serial number",
            "app": "Application",
        }
        widgets = {
            "device_sn": forms.TextInput(attrs={"placeholder": "e.g. SN-12345"}),
            "details": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Optional notes, e.g. Windows 11 / macOS 15"}
            ),
        }
        error_messages = {
            "device_sn": {"required": "Device serial number is required."},
            "app": {"required": "Application is required."},
        }
