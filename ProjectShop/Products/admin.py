from django.contrib import admin
from .models import Products, Client, Categories, Basket, History_transactions, Delivery

# Register your models here.
admin.site.register(Products)
admin.site.register(Client)
admin.site.register(Categories)
admin.site.register(Basket)
admin.site.register(History_transactions)
admin.site.register(Delivery)