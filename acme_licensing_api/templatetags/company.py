from django import template
from django.conf import settings

register = template.Library()

# used to set company name where needed
@register.simple_tag
def company_name():
    return settings.COMPANY_NAME
