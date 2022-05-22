

from django.contrib import admin
from django.urls import path, include
#
# from ProjectShop.Products.views import ProductCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('Products.urls')),
    # path('product-create', ProductCreateView.as_view(), name="product_create"),
]
