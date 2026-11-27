from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from accounts.models import User

from django.conf import settings

class CompanyNameRuleTests(TestCase):
    def test_distributor_without_company_name_is_invalid(self):
        user = User(username="acme", is_company=True, password="x")
        with self.assertRaises(ValidationError) as ctx:
            user.full_clean()
        self.assertIn("company_name", ctx.exception.message_dict)

    def test_distributor_with_company_name_is_valid(self):
        user = User(username="acme", is_company=True, company_name=settings.COMPANY_NAME, password="x")
        user.full_clean()

    def test_create_user_without_company_name_is_rejected(self):
        with self.assertRaises(ValidationError):
            User.objects.create_user(username="acme", is_company=True, password="x")


class LoginFlowTests(TestCase):
    def test_login_page_renders_and_login_redirects_home(self):
        User.objects.create_user(username="acme", password="x")
        response = self.client.get("/accounts/login/")
        self.assertContains(response, "Log in")
        response = self.client.post(
            "/accounts/login/", {"username": "acme", "password": "x"}
        )
        self.assertRedirects(response, reverse(settings.LOGIN_REDIRECT_URL))
