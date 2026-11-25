from django.urls import path, include
from exceptionlog.views import (
    ExceptionLogListView,
    ExceptionLogCreateView,
    ExceptionLogDetailView,
    ExceptionLogDeleteView,
)

urlpatterns = [
    path('', ExceptionLogListView.as_view(), name='exceptionlog-list'),
    path('create/', ExceptionLogCreateView.as_view(), name='exceptionlog-create'),
    path('<int:pk>/', include([
        path('', ExceptionLogDetailView.as_view(), name='exceptionlog-details'),
        path('delete/', ExceptionLogDeleteView.as_view(), name='exceptionlog-delete'),
    ])),
]
