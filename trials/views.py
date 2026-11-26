from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from trials.models import Trial


class TrialListView(ListView):
    model = Trial


class TrialDetailView(DetailView):
    model = Trial


class TrialCreateView(CreateView):
    model = Trial
    fields = ["device_sn", "app", "details"]
    success_url = reverse_lazy("trial-list")


class TrialUpdateView(UpdateView):
    model = Trial
    fields = ["device_sn", "app", "details"]
    success_url = reverse_lazy("trial-list")
