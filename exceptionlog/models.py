from django.db import models

from acme_licensing_api.validators import app_version_validator
from products.models import Product


# this is exception log, submitted from deployed apps
class ExceptionLog(models.Model):

    class Level(models.TextChoices):
        DEBUG = 'DEBUG', 'Debug'
        INFO = 'INFO', 'Info'
        WARNING = 'WARNING', 'Warning'
        ERROR = 'ERROR', 'Error'
        SEVERE = 'SEVERE', 'Severe'
        CRITICAL = 'CRITICAL', 'Critical'

    class Meta:
        ordering = ['-timestamp']
        indexes = [
            # composite index for queries
            models.Index(fields=['app', 'timestamp'], name='exlog_app_time_idx'),
        ]

    # optional client IP
    ip = models.GenericIPAddressField(
        null=True,
        blank=True,
        verbose_name="Client IP",
        help_text="IP address of the client (optional).",
    )

    app = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='exceptions',
        help_text="Product, reported the exception.",
    )

    version = models.CharField(
        max_length=20,
        default="",
        validators=[
            app_version_validator()
        ],
        help_text="Version of the reporting application, e.g. 1.2.3.",
    )

    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    level = models.CharField(
        max_length=10,
        choices=Level.choices,
        error_messages={
            "required": "Severity level required.",
        },
        help_text="Severity level.",
    )

    message = models.CharField(
        max_length=200,
        error_messages={
            "required": "Message required.",
        },
        help_text="Message",
    )

    # optional stacktrace
    stacktrace = models.TextField(
        default="",
        blank=True,
        help_text="Optional full stack trace.",
    )

    def __str__(self):
        return f"{self.timestamp.isoformat()} [{self.level}] {self.message[:60]}"
