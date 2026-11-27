from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from customers.forms import CustomerForm
from customers.models import Customer


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer

    def get_queryset(self):
        # the detail page renders the customer's licenses table
        return super().get_queryset().prefetch_related("licenses__trial__app")


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy("customers-list")


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy("customers-list")


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy("customers-list")
