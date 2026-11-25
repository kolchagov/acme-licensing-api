from django.urls import path, include

from customers.views import *

urlpatterns = [
    path('', CustomerListView.as_view(), name='customers-list'),
    path('create', CustomerCreateView.as_view(), name='customer-create'),
    path('<int:pk>/', include([
        path('', CustomerDetailView.as_view(), name='customer-detail'),
        path('update', CustomerUpdateView.as_view(), name='customer-update'),
        path('delete', CustomerDeleteView.as_view(), name='customer-delete'),
    ]))
]