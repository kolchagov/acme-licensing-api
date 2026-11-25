
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from products.models import Product

class ProductsListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

class ProductUpdateView(UpdateView):
    model = Product
    fields = ["code", "name", "url", "description"]
    success_url = reverse_lazy("product-list")

class ProductCreateView(CreateView):
    model = Product
    fields = ["code", "name", "url", "description"]
    success_url = reverse_lazy("product-list")

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("product-list")