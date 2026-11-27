from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from trials.forms import TrialForm
from trials.models import Trial


class TrialListView(LoginRequiredMixin, ListView):
    model = Trial


class TrialDetailView(LoginRequiredMixin, DetailView):
    model = Trial


class TrialCreateView(LoginRequiredMixin, CreateView):
    model = Trial
    form_class = TrialForm
    success_url = reverse_lazy("trial-list")


class TrialUpdateView(LoginRequiredMixin, UpdateView):
    model = Trial
    form_class = TrialForm
    success_url = reverse_lazy("trial-list")


class TrialDeleteView(LoginRequiredMixin, DeleteView):
    model = Trial
    success_url = reverse_lazy("trial-list")
