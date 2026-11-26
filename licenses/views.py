from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from licenses.models import License

FIELDS = ["trial", "customer", "version", "expiry_date"]


class LicenseListView(ListView):
    model = License

class LicenseDetailView(DetailView):
    model = License

class LicenseCreateView(CreateView):
    model = License
    fields = FIELDS
    success_url = reverse_lazy("license-list")

class LicenseUpdateView(UpdateView):
    model = License
    fields = FIELDS
    success_url = reverse_lazy("license-list")

class LicenseDeleteView(DeleteView):
    model = License
    success_url = reverse_lazy("license-list")
