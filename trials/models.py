from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models

from products.models import Product
from acme_licensing_api.utils import trial_code_generator

class Trial(models.Model):
    class Meta:
        ordering = ['-date_installed']
        constraints = [
            models.UniqueConstraint(
                fields=['app', 'device_sn'],
                name='Trial must be unique per app and device',
            ),
        ]

    device_sn = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(regex=r'^[a-zA-Z0-9_-]+$', message='Enter a valid device SN.'),
            MinLengthValidator(3, message='Minimum 3 characters.'),
        ]
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

    @property
    def trial_code(self):
        return trial_code_generator(self)

    def __str__(self):
        return f"{self.device_sn} ({self.app.name}) {self.date_installed.isoformat()}"
