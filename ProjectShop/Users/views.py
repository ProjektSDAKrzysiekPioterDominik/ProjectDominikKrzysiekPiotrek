from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from Users.forms import SignUpForm #type: ignore
from django.contrib import auth
from django.shortcuts import render
from Products.models import Basket, Client #type: ignore


from django.contrib.auth.decorators import login_required

class Login_user(LoginView):
    template_name = 'login.html'

class SignUpView(CreateView):
    template_name = 'sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')

def logoutview(request):
    auth.logout(request);
    return redirect('/')

@login_required(login_url='login')
def user_side(request, id):
    Client_rambo = Client.objects.get(user = id)
    Client_rambo_id = Client_rambo.id
    Basket_rambo = Basket.objects.filter(Id_client = Client_rambo_id)
    data = {"Client_rambo": Client_rambo, 'Basket_rambo': Basket_rambo}
    return render(request, 'user_side.html', data)