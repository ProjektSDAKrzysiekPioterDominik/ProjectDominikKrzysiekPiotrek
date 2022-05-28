from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from Products.forms import ProductForm
from django.http import HttpResponse
from .models import Products


class ProductCreateView(CreateView):
    template_name = "product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("home")


def index(request):
    zapytanie = Products.objects.all()
    return HttpResponse(zapytanie)

def get_hello(request):
    data = {}
    return render(request, 'base.html', data)

class ProductSearchView(ListView):
    model = Products
    template_name = 'Search.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Products.objects.filter(Product_name__icontains=query).filter(Is_listed = True).order_by('-Date_added')
        else:
            return Products.objects.all()