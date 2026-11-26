from django.core.validators import MinLengthValidator
from django.db import models

from acme_licensing_api.validators import app_version_validator
from products.models import Product


# this is exception log, submitted from deployed apps
class ExceptionLog(models.Model):

    # optional client IP
    ip = models.GenericIPAddressField(
        null=True,
        blank=True,
    )

    app = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='exceptions'
    )

    version = models.CharField(
        max_length=10,
        default="",
        validators=[
            app_version_validator()
        ]
    )

    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    level = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(4, message="Severity level required.")
        ]
    )

    message = models.CharField(
        max_length=200,
        error_messages={
            "required": "Message required.",
        }
    )

    # optional stacktrace
    stacktrace = models.TextField(
        default="",
        blank=True,
    )
