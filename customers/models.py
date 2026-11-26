from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


class Customer(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(5, 'Enter valid customer or company name (min 5 chars)'),
        ],
        help_text="Customer or company name as it should appear on invoices.",
    )
    address = models.CharField(
        max_length=100,
        blank=True,
        validators=[
            MinLengthValidator(5, 'Enter valid address or leave empty (min 5 chars)'),
        ],
        help_text="Billing address (optional).",
    )

    contact_person = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(5, 'Enter valid contact name (min 5 chars)'),
        ],
        help_text="Person responsible for this account.",
    )

    uic = models.CharField(
        max_length=13,
        unique=True,
        verbose_name="UIC",
        validators=[
            RegexValidator(r'^\d{9,13}$', message='Enter valid UIC number (min 9 digits)')
        ],
        error_messages={
            'unique': 'A customer with this UIC already exists.',
        },
        help_text="Company identification number, 9 to 13 digits.",
    )

    vat = models.CharField(
        max_length=11,
        unique=True,
        verbose_name="VAT number",
        validators=[
            RegexValidator(
                r'^[A-Z]{2}\d{9}$',
                message='Enter a valid VAT number (two letters and 9 digits).',
            )
        ],
        error_messages={
            'unique': 'A customer with this VAT number already exists.',
        },
        help_text="Two-letter country code followed by 9 digits, e.g. BG123456789.",
    )

    phone = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(r'^\+?[0-9\s]{9,15}$',
                           message='Enter valid phone number')
        ],
        help_text="Contact phone, 9 to 15 digits with optional leading +.",
    )
    email = models.EmailField(
        max_length=100,
        help_text="Email used for license delivery and invoices.",
    )

    # products this customer is entitled to
    products = models.ManyToManyField(
        'products.Product',
        blank=True,
        related_name='customers',
        help_text="Products this customer is entitled to.",
    )

    def __str__(self):
        return self.name
