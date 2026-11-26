from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models


# defines a software product

class Product(models.Model):
    # code is composed by a letter and two digits
    code = models.CharField(
        max_length=3,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[A-Z]\d{2}$',
                message="Product code should contain one letter and two digits."
            )
        ],
        help_text="One uppercase letter followed by two digits, e.g. A01.",
    )

    name = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(5, message="Enter a valid product name.")
        ],
        help_text="Public product name.",
    )

    # product page link
    url = models.URLField(
        max_length=200,
        blank=True,
        verbose_name="Product URL",
        help_text="Public product page (optional).",
    )

    description = models.TextField(
        blank=True,
        help_text="Short description shown to customers.",
    )

    # other products sold together with this one (bundle)
    bundled_products = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
        related_name='bundled_in',
        help_text="Other products sold together with this one.",
    )

    def __str__(self):
        return f"{self.code} - {self.name}"
