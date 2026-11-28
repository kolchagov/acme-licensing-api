from django.contrib import admin

from accounts.models import User
from accounts.forms import UserDetailForm


@admin.register(User)
class UserDetailAdmin(admin.ModelAdmin):
    form = UserDetailForm
    list_display = ( "username", "get_full_name", "is_company", "logo", "company_name", "iban")
