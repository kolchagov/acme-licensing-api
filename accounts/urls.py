from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.forms import LoginForm
from accounts.views import RegisterView, AccountListView

urlpatterns = [
    path('', AccountListView.as_view(), name='account-list'),
    path('login/', LoginView.as_view(authentication_form=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
