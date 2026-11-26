from datetime import date

from django.core.exceptions import ValidationError
from django.test import TestCase

from licenses.models import License


class ExpiryDateTests(TestCase):
    def test_expiry_before_license_date_is_rejected(self):
        license = License(version="1.0.0")
        license.license_date = date(2026, 1, 2)
        license.expiry_date = date(2026, 1, 1)
        with self.assertRaises(ValidationError):
            license.clean()

    def test_expiry_after_license_date_is_valid(self):
        license = License(version="1.0.0")
        license.license_date = date(2026, 1, 2)
        license.expiry_date = date(2026, 1, 3)
        license.clean()
