from django.urls import path, include

from licenses.views import *

urlpatterns = [
    path('', LicenseListView.as_view(), name='license-list'),
    path('create', LicenseCreateView.as_view(), name='license-create'),
    path('<int:pk>/', include([
        path('', LicenseDetailView.as_view(), name='license-detail'),
        path('update', LicenseUpdateView.as_view(), name='license-update'),
        path('delete', LicenseDeleteView.as_view(), name='license-delete'),
    ]))
]
