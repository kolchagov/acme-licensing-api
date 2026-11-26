from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


class Customer(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(5, 'Enter valid customer or company name (min 5 chars)'),
        ]
    )
    address = models.CharField(
        max_length=100,
        blank=True,
        validators=[
            MinLengthValidator(5, 'Enter valid address or leave empty (min 5 chars)'),
        ],
    )

    contact_person = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(5, 'Enter valid contact name (min 5 chars)'),
        ]
    )

    uic = models.CharField(
        max_length=13,
        unique=True,
        validators=[
            RegexValidator(r'^\d{9,13}$', message='Enter valid UIC number (min 9 digits)')
        ],
        error_messages={
            'unique': 'A customer with this UIC already exists.',
        },
    )

    vat = models.CharField(
        max_length=11,
        unique=True,
        validators=[
            RegexValidator(
                r'^[A-Z]{2}\d{9}$',
                message='Enter a valid VAT number (two letters and 9 digits).',
            )
        ],
        error_messages={
            'unique': 'A customer with this VAT number already exists.',
        },
    )

    phone = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(r'^\+?[0-9\s]{9,15}$',
                           message='Enter valid phone number')
        ]
    )
    email = models.EmailField(
        max_length=100,
    )

    # products this customer is entitled to
    products = models.ManyToManyField(
        'products.Product',
        blank=True,
        related_name='customers',
    )

    def __str__(self):
        return self.name

