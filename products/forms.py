from django import forms

from acme_licensing_api.forms import BootstrapForm
from products.models import Product


class ProductForm(BootstrapForm, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # a product cannot bundle itself
        if self.instance.pk:
            self.fields["bundled_products"].queryset = (
                Product.objects.exclude(pk=self.instance.pk))

    # clean code
    def clean(self):
        cleaned = super().clean()
        code = cleaned.get("code")
        if code:
            cleaned["code"] = code.upper()
        bundled = cleaned.get("bundled_products")
        if bundled is not None and len(bundled) == 1:
            self.add_error("bundled_products",
                           "A bundled product requires more than one product.")
        return cleaned

    class Meta:
        model = Product
        fields = ["code", "name", "url", "description", "bundled_products"]
