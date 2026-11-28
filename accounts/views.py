from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from accounts.forms import RegisterForm

UserModel = get_user_model()


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class AccountListView(ListView):
    model = UserModel
    template_name = 'accounts/account_list.html'
