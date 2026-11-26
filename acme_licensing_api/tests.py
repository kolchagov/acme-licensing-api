from django.test import SimpleTestCase

from acme_licensing_api.utils import luhn_checksum, is_luhn_valid


class LuhnTests(SimpleTestCase):
    def test_check_digit_validates(self):
        base = "11010001"
        self.assertEqual(luhn_checksum(base), 3)
        self.assertTrue(is_luhn_valid(base + str(luhn_checksum(base))))
        self.assertFalse(is_luhn_valid("110100015"))
        self.assertTrue(is_luhn_valid("110100013"))
