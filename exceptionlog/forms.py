from django import forms

from acme_licensing_api.forms import BootstrapForm
from exceptionlog.models import ExceptionLog


class ExceptionLogForm(BootstrapForm, forms.ModelForm):
    class Meta:
        model = ExceptionLog
        fields = ["ip", "app", "version", "level", "message", "stacktrace"]
        labels = {
            "ip": "Client IP",
            "app": "Application",
            "message": "Error message",
        }
        widgets = {
            "ip": forms.TextInput(attrs={"placeholder": "e.g. 192.168.0.10"}),
            "version": forms.TextInput(attrs={"placeholder": "e.g. 1.2.3"}),
            "message": forms.TextInput(attrs={"placeholder": "Exception message"}),
            "stacktrace": forms.Textarea(
                attrs={"rows": 5, "placeholder": "Paste the full stack trace here (optional)"}
            ),
        }
        error_messages = {
            "app": {"required": "Application is required."},
            "version": {"required": "Version is required."},
            "level": {"required": "Severity level required."},
            "message": {"required": "Message required."},
        }
