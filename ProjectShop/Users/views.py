from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from Users.forms import SignUpForm #type: ignore

class Login_user(LoginView):
    template_name = 'login.html'

class SignUpView(CreateView):
    template_name = 'sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')
