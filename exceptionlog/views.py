from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView

from exceptionlog.forms import ExceptionLogForm
from exceptionlog.models import ExceptionLog


class ExceptionLogListView(LoginRequiredMixin, ListView):
    model = ExceptionLog
    ordering = ["-timestamp"]


class ExceptionLogCreateView(LoginRequiredMixin, CreateView):
    model = ExceptionLog
    form_class = ExceptionLogForm
    success_url = reverse_lazy("exceptionlog-list")


class ExceptionLogDetailView(LoginRequiredMixin, DetailView):
    model = ExceptionLog


class ExceptionLogDeleteView(LoginRequiredMixin, DeleteView):
    model = ExceptionLog
    success_url = reverse_lazy("exceptionlog-list")
