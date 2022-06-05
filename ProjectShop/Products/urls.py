from django.urls import path


from Products.views import ProductCreateView, NewBasketItemView2  # type: ignore

from Products.views import index, ProductSearchView, all_products_for_category,product, NewBasketItemView #type: ignore



urlpatterns = [
    path('product-create/', ProductCreateView.as_view(), name="product_create"),
    path('category/<category_id>/', all_products_for_category, name="all-for-category"),
    path('product/<id>/', product, name="product"),
    path('', index),
    path('search-products/', ProductSearchView.as_view(), name='search_products'),
    path('add-to-basket/', NewBasketItemView.as_view(), name='add_to_basket'),
    path('add-to-basket2/', NewBasketItemView2.as_view(), name='add_to_basket2'),
]
