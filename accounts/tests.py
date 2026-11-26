from django.core.exceptions import ValidationError
from django.test import TestCase

from accounts.models import User


class CompanyNameRuleTests(TestCase):
    def test_distributor_without_company_name_is_invalid(self):
        user = User(username="acme", is_company=True, password="x")
        with self.assertRaises(ValidationError) as ctx:
            user.full_clean()
        self.assertIn("company_name", ctx.exception.message_dict)

    def test_distributor_with_company_name_is_valid(self):
        user = User(username="acme", is_company=True, company_name="Acme Ltd.", password="x")
        user.full_clean()

    def test_create_user_without_company_name_is_rejected(self):
        with self.assertRaises(ValidationError):
            User.objects.create_user(username="acme", is_company=True, password="x")
