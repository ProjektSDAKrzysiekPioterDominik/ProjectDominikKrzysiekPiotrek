from django.urls import path


from Products.views import ProductCreateView #type: ignore

from Products.views import index, ProductSearchView #type: ignore



urlpatterns = [
    path('product-create/', ProductCreateView.as_view(), name="product_create"),
    path('products', index),
    path('search-products/', ProductSearchView.as_view(), name='search_products')
]