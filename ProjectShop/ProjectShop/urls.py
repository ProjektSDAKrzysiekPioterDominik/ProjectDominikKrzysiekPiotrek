

from django.contrib import admin
from django.urls import path, include
from Products.views import get_hello

# from ProjectShop.Products.views import ProductCreateView

urlpatterns = [
    path('', get_hello, name = 'home'),
    path('admin/', admin.site.urls),
    path('products/', include('Products.urls')),
    path('shop_users/', include('Users.urls')),
    # path('product-create', ProductCreateView.as_view(), name="product_create"),
]
