from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView

from exceptionlog.forms import ExceptionLogForm
from exceptionlog.models import ExceptionLog


class ExceptionLogListView(ListView):
    model = ExceptionLog
    ordering = ["-timestamp"]


class ExceptionLogCreateView(CreateView):
    model = ExceptionLog
    form_class = ExceptionLogForm
    success_url = reverse_lazy("exceptionlog-list")


class ExceptionLogDetailView(DetailView):
    model = ExceptionLog


class ExceptionLogDeleteView(DeleteView):
    model = ExceptionLog
    success_url = reverse_lazy("exceptionlog-list")
