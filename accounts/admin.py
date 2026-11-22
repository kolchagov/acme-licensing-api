from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import AccountDetailForm
from accounts.models import AccountDetail, User

admin.site.register(User, UserAdmin)


@admin.register(AccountDetail)
class AccountDetailAdmin(admin.ModelAdmin):
    form = AccountDetailForm
    list_display = ("user", "company_name", "iban")
