from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from acme_licensing_api.utils import trial_code_generator
from acme_licensing_api.validators import app_version_validator
from customers.models import Customer
from trials.models import Trial

class License(models.Model):
    trial = models.OneToOneField(
        to=Trial,
        on_delete=models.CASCADE,
        related_name='license',
    )

    customer = models.ForeignKey(
        to=Customer,
        on_delete=models.CASCADE,
        related_name='licenses',
    )

    version = models.CharField(
        max_length=10,
        validators=[
            app_version_validator()
        ],
    )

    license_date = models.DateField(
        auto_now_add=True,
    )

    # optional expiration date
    expiry_date = models.DateField(
        blank=True,
        null=True,
    )

    @property
    def check_code(self):
        return trial_code_generator(self.trial)

    def clean(self):
        super().clean()
        # license_date is auto_now_add (today)
        start = self.license_date or timezone.localdate()
        if self.expiry_date and self.expiry_date < start:
            raise ValidationError({
                'expiry_date': 'Expiry date cannot be earlier than the license date.',
            })

    def __str__(self):
        return f"{self.customer.name} - {self.trial.app.name} - ID:{self.id} {self.license_date.isoformat()}"
