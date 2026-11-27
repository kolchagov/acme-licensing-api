from django import forms

from acme_licensing_api.forms import BootstrapForm
from customers.models import Customer


class CustomerForm(BootstrapForm, forms.ModelForm):

    def clean(self):
        cleaned = super().clean()
        uic = (cleaned.get("uic") or "").strip()
        vat = (cleaned.get("vat") or "").strip().upper()
        cleaned["uic"] = uic
        cleaned["vat"] = vat
        # a Bulgarian VAT number embeds the 9-digit UIC
        if vat.startswith("BG") and len(uic) == 9 and vat[2:] != uic:
            self.add_error("vat", "VAT number must match the UIC for Bulgarian customers.")
        return cleaned

    class Meta:
        model = Customer
        fields = ["name", "address", "contact_person", "uic", "vat", "phone", "email"]
        labels = {
            "name": "Customer name",
            "address": "Billing address",
            "uic": "UIC",
            "vat": "VAT number",
            "phone": "Phone number",
        }
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "e.g. Techno Market Ltd."}),
            "address": forms.TextInput(attrs={"placeholder": "e.g. 12 Vitosha Blvd., Sofia"}),
            "contact_person": forms.TextInput(attrs={"placeholder": "e.g. Ivan Petrov"}),
            "uic": forms.TextInput(attrs={"placeholder": "9 to 13 digits"}),
            "vat": forms.TextInput(attrs={"placeholder": "e.g. BG203456789"}),
            "phone": forms.TextInput(attrs={"placeholder": "e.g. +359 2 9876543"}),
            "email": forms.EmailInput(attrs={"placeholder": "e.g. office@company.bg"}),
        }
        error_messages = {
            "name": {"required": "Customer name is required."},
            "contact_person": {"required": "Contact person is required."},
            "uic": {"required": "UIC is required."},
            "vat": {"required": "VAT number is required."},
            "phone": {"required": "Phone number is required."},
            "email": {
                "required": "Email is required.",
                "invalid": "Enter a valid email address.",
            },
        }
