from django.urls import path

from Products.views import ProductCreateView
from Products.views import index


urlpatterns = [
    path('product-create/', ProductCreateView.as_view(), name="product_create"),
    path('products', index),
]