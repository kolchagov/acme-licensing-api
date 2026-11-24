from msilib.schema import ListView

from django.shortcuts import render
from django.views.generic import DetailView

from models import Product

class ProductsListView(ListView):
    model = Product
    # TODO add template

class ProductDetailView(DetailView):
    model = Product
    # TODO template

class ProductUpdateView(UpdateView):
    model = Product
    # TODO