from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
from django.utils.functional import empty


class Customer(models.Model):
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
        validators=[
            RegexValidator(r'^\d{9,13}$', message='Enter valid UIC number (min 9 digits)')
        ],
    )

    vat = models.CharField(
        max_length=11,
        validators=[
            RegexValidator(r'\w{2}\d{9}')
        ]
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

