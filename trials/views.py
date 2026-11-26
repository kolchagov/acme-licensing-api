from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from trials.forms import TrialForm
from trials.models import Trial


class TrialListView(ListView):
    model = Trial


class TrialDetailView(DetailView):
    model = Trial


class TrialCreateView(CreateView):
    model = Trial
    form_class = TrialForm
    success_url = reverse_lazy("trial-list")


class TrialUpdateView(UpdateView):
    model = Trial
    form_class = TrialForm
    success_url = reverse_lazy("trial-list")


class TrialDeleteView(DeleteView):
    model = Trial
    success_url = reverse_lazy("trial-list")
