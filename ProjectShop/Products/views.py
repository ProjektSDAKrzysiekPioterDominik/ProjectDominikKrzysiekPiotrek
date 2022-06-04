from django.shortcuts import render, redirect
from django.views import View

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

    data = {'all_products': all_products}
    return render(request, 'szablon.html', data)

def all_products_for_category(request, category_id):
    all_products_for_category = Products.objects.filter(Id_category=category_id).order_by('-Date_added')
    return render(request, 'all-products-for-categories.html', {"products": all_products_for_category})

def categorie(request):
    categories = Categories.objects.all()
    data = {'categories': categories}
    return render(request, 'categories.html', data)

def product(request,id):
    product = Products.objects.get(pk=id)
    data = {'product': product}
    return render(request, 'product.html', data)

def get_hello(request):
    categories = Categories.objects.all()
    data = {'categories': categories}
    return render(request, 'index.html', data)

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


class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        print(product)
        return redirect('home')
    # def get(self, request):
    #     get_products = None
    #     get_category = Categories.get