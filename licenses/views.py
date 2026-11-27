from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from licenses.forms import LicenseForm
from licenses.models import License


class LicenseListView(LoginRequiredMixin, ListView):
    model = License


class LicenseDetailView(LoginRequiredMixin, DetailView):
    model = License


class LicenseCreateView(LoginRequiredMixin, CreateView):
    model = License
    form_class = LicenseForm
    success_url = reverse_lazy("license-list")


class LicenseUpdateView(LoginRequiredMixin, UpdateView):
    model = License
    form_class = LicenseForm
    success_url = reverse_lazy("license-list")


class LicenseDeleteView(LoginRequiredMixin, DeleteView):
    model = License
    success_url = reverse_lazy("license-list")
