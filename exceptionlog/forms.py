from django import forms

from acme_licensing_api.forms import BootstrapForm
from exceptionlog.models import ExceptionLog


class ExceptionLogForm(BootstrapForm, forms.ModelForm):
    class Meta:
        model = ExceptionLog
        fields = ["ip", "app", "version", "level", "message", "stacktrace"]
        widgets = {
            "stacktrace": forms.Textarea(attrs={"rows": 5}),
        }
