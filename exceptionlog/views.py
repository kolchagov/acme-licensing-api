from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView

from exceptionlog.models import ExceptionLog

FIELDS = ["ip", "app", "level", "message", "stacktrace"]


class ExceptionLogListView(ListView):
    model = ExceptionLog
    ordering = ["-timestamp"]

class ExceptionLogCreateView(CreateView):
    model = ExceptionLog
    fields = FIELDS
    success_url = reverse_lazy("exceptionlog-list")

class ExceptionLogDetailView(DetailView):
    model = ExceptionLog

class ExceptionLogDeleteView(DeleteView):
    model = ExceptionLog
    success_url = reverse_lazy("exceptionlog-list")
