from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from customers.models import Customer

FIELDS = ["name", "address", "contact_person", "uic", "vat", "phone", "email"]


class CustomerListView(ListView):
    model = Customer

class CustomerDetailView(DetailView):
    model = Customer

class CustomerCreateView(CreateView):
    model = Customer
    fields = FIELDS
    success_url = reverse_lazy("customers-list")

class CustomerUpdateView(UpdateView):
    model = Customer
    fields = FIELDS
    success_url = reverse_lazy("customers-list")

class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy("customers-list")
