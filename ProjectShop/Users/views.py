from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from Users.forms import SignUpForm #type: ignore
from django.contrib import auth
from django.shortcuts import render

class Login_user(LoginView):
    template_name = 'login.html'

class SignUpView(CreateView):
    template_name = 'sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')

def logoutview(request):
    auth.logout(request);
    return redirect('/')

def user_side(request):
    data = {}
    return render(request, 'user_side.html', data)