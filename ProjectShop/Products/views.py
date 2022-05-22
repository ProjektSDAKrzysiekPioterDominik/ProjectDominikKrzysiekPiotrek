from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from django.urls import reverse_lazy
from Products.forms import ProductForm
from django.http import HttpResponse
from .models import Products


class ProductCreateView(CreateView):
    template_name = "product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("book_create")


def index(request):
    zapytanie = Products.objects.all()
    return HttpResponse(zapytanie)

def get_hello(request):
    data = {}
    return render(request, 'base.html', data)

