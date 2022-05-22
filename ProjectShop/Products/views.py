from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from django.urls import reverse_lazy
from Products.forms import ProductForm


class ProductCreateView(CreateView):
    template_name = "product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("book_create")


def get_hello(request):
    data = {}
    return render(request, 'base.html', data)