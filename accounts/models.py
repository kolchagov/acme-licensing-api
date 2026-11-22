from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models
from django.db.models import OneToOneField, CharField
from django.db.models.fields.files import ImageField


class UserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username must be set")
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    objects = UserManager()


class AccountDetail(models.Model):
    user = OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="details",
        primary_key=True
    )
    company_name = CharField(
        max_length=255,
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(5, message="Enter a valid Company Name."),
        ],
    )
    logo = ImageField(
        upload_to="account_logos/",
        blank=True,
        null=True
    )
    iban = CharField(
        max_length=34,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                r'^[A-Z]{2}\d{2}[A-Z0-9]{11,30}$',
                message="Enter a valid Bank Account."
            )
        ]
    )

    def __str__(self):
        return self.company_name if self.company_name else self.user.username
