from django.db import models

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

    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    level = models.CharField(
        max_length=10,
    )

    message = models.CharField(
        max_length=200,
    )

    # optional stacktrace
    stacktrace = models.TextField(
        default="",
        blank=True,
    )
