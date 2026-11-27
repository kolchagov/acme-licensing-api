from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from products.models import Product


def home_view(request: HttpRequest) -> HttpResponse:
    context = {'products': Product.objects.order_by('code')}
    return render(request, 'home.html', context)
