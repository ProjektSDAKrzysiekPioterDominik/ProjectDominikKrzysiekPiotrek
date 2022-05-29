from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from Products.forms import ProductForm  #type: ignore
from django.http import HttpResponse
from .models import Products,Categories,Producer


class ProductCreateView(CreateView):
    template_name = "product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("home")


def index(request):
    all_products = Products.objects.all()
    first = Products.objects.get(pk=1)
    catego = Products.objects.filter(Id_category=2)
    producer = Products.objects.filter(Producer=8)
    catego_name = Categories.objects.get(id=2)
    categories = Categories.objects.all()
    null = Products.objects.filter(Id_category__isnull=False)
    have = Products.objects.filter(Describe__icontains='lekko')
    #return HttpResponse(all_products)

    #context = {'categories' : categories}
    return render(request,)

def categorie(request, id):
    categorie_user = Categories.objects.get(pk=id)
    return HttpResponse(categorie_user.Name)

def product(request,id):
    product_user = Products.objects.get(pk=id)
    textwrap = "<h1>" + str(product_user) + "</h1>" + \
               "<p>" + str(product_user.Describe) + "</p>" + \
               "<p>" + str(product_user.Price) + "</p>"
    return HttpResponse(product_user)

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
            return Products.objects.filter(Product_name__icontains=query).order_by('-Date_added')
        else:
            return Products.objects.all()