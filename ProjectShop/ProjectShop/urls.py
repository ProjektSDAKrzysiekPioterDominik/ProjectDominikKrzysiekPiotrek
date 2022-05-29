

from django.contrib import admin
from django.urls import path, include
from Products.views import get_hello
from Products.views import *
# from ProjectShop.Products.views import ProductCreateView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', get_hello, name = 'home'),
    path('admin/', admin.site.urls),
    path('products/', include('Products.urls')),
    path('products-list/', index, name='index'),
    #path('categorie/<id>/', categorie, name='categorie'),
    path('categorie/', categorie, name='categorie'),
    path('product/<id>/', product, name='product'),

    # path('product-create', ProductCreateView.as_view(), name="product_create"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)