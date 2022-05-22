from django.urls import path

from Products.views import ProductCreateView #type: ignore

urlpatterns = [
    path('product-create/', ProductCreateView.as_view(), name="product_create"),
]