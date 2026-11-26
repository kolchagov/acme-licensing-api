from django import forms

from acme_licensing_api.forms import BootstrapForm
from customers.models import Customer


class CustomerForm(BootstrapForm, forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "address", "contact_person", "uic", "vat", "phone", "email"]
