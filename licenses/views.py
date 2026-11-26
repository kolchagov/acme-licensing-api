from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from licenses.forms import LicenseForm
from licenses.models import License


class LicenseListView(ListView):
    model = License


class LicenseDetailView(DetailView):
    model = License


class LicenseCreateView(CreateView):
    model = License
    form_class = LicenseForm
    success_url = reverse_lazy("license-list")


class LicenseUpdateView(UpdateView):
    model = License
    form_class = LicenseForm
    success_url = reverse_lazy("license-list")


class LicenseDeleteView(DeleteView):
    model = License
    success_url = reverse_lazy("license-list")
