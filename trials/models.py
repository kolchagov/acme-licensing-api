from django.db import models

from products.models import Product


class Trial(models.Model):
    device_sn = models.CharField(
        max_length=50,
    )

    app = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='trials',
    )

    date_installed = models.DateField(
        auto_now_add=True
    )

    # optional details
    details = models.TextField(
        blank=True,
        default='',
    )