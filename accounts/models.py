from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models

class User(AbstractUser):
    is_company = models.BooleanField(
        default=False,
        verbose_name="Company account",
        help_text="Check if this account represents a distributor or our staff.",
    )

    company_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(5, message="Enter a valid Company Name."),
        ],
        help_text="Legal name of the company, required for distributors.",
    )
    logo = models.ImageField(
        upload_to="account_logos/",
        blank=True,
        null=True,
        help_text="Company logo.",
    )
    iban = models.CharField(
        max_length=34,
        blank=True,
        null=True,
        verbose_name="IBAN",
        validators=[
            RegexValidator(
                r'^[A-Z]{2}\d{2}[A-Z0-9]{11,30}$',
                message="Enter a valid Bank Account."
            )
        ],
        help_text="IBAN for invoicing, e.g. BG00ABCD1234567890.",
    )

    def __str__(self):
        return self.company_name or self.username

    def clean(self):
        super().clean()
        if self.is_company and not self.company_name:
            raise ValidationError({
                'company_name': 'Company name is required for distributors.',
            })
