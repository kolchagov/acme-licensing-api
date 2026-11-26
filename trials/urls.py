from django.urls import path, include

from trials.views import (
    TrialListView,
    TrialCreateView,
    TrialDetailView,
    TrialUpdateView,
    TrialDeleteView,
)

urlpatterns = [
    path('', TrialListView.as_view(), name='trial-list'),
    path('create/', TrialCreateView.as_view(), name='trial-create'),
    path('<int:pk>/', include([
        path('', TrialDetailView.as_view(), name='trial-detail'),
        path('edit/', TrialUpdateView.as_view(), name='trial-edit'),
        path('delete/', TrialDeleteView.as_view(), name='trial-delete'),
    ])),
]
