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
        ]
    )

    name = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(5, message="Enter a valid product name.")
        ]
    )

    # product page link
    url = models.URLField(
        max_length=200,
        blank=True,
    )

    description = models.TextField(
        blank=True,
    )
