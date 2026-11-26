from django import forms


class BootstrapForm:
    """Mixin: adds Bootstrap classes to every widget of a Form or ModelForm."""

    template_name = 'bs5/form.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.CheckboxInput):
                css = 'form-check-input'
            elif isinstance(field.widget, (forms.Select, forms.SelectMultiple)):
                css = 'form-select'
            else:
                css = 'form-control'
            field.widget.attrs.setdefault('class', css)
        if self.is_bound:
            for name in self.errors:
                if name in self.fields:
                    self.fields[name].widget.attrs['class'] += ' is-invalid'
