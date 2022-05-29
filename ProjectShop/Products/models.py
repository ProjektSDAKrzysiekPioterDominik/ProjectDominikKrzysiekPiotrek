from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    Login = models.TextField(max_length = 20)
    Name = models.TextField(max_length = 20)
    Surname = models.TextField(max_length = 20)
    Adress = models.TextField(max_length = 100)
    Email = models.TextField(max_length = 20)
    Phone = models.TextField(max_length = 20)
    Birth_date = models.DateField()
    City = models.TextField(max_length = 20)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

class Categories(models.Model):
    Name = models.CharField(max_length = 100)

    def __str__(self):
        return f"{self.Name}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Producer(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=60)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Producer"
        verbose_name_plural = "Producers"

class Products(models.Model):
    Id_category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    Product_name = models.CharField(max_length=100)
    Producer = models.ForeignKey(Producer, on_delete=models.CASCADE,null=True, blank=True)
    Price = models.DecimalField(default=0, validators=[MinValueValidator(0.01)], max_digits=12, decimal_places=2)
    Image = models.ImageField(blank=True)
    Describe = models.TextField(max_length=500)
    Date_added = models.DateTimeField(blank = True, null = True, auto_now_add=True)
    Is_listed = models.BooleanField()
    Id_client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f"{self.Product_name} - {self.Price} PLN - {self.Is_listed} - {self.Image}"

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Basket(models.Model):
    Id_product = models.ForeignKey(Products, on_delete=models.CASCADE,null =True)
    Id_client = models.ForeignKey(Client, on_delete=models.CASCADE,null =True)
    Quantity = models.IntegerField()
    Price = models.DecimalField(max_digits = 12, decimal_places = 2)

    class Meta:
        verbose_name = "Basket"
        verbose_name_plural = "Baskets"

class Delivery(models.Model):
    Name = models.TextField(max_length = 1000)
    Surname = models.TextField(max_length = 1000)
    Company_name = models.TextField(max_length = 1000)
    Phone = models.TextField(max_length = 1000)
    Email = models.TextField(max_length = 1000)

    class Meta:
        verbose_name = "Delivery"
        verbose_name_plural = "Deliveries"

class History_transactions(models.Model):
    Id_client = models.ForeignKey(Client, on_delete=models.CASCADE,null =True)
    Date_of_buy = models.DateField()
    Price = models.DecimalField(max_digits = 12, decimal_places = 2)
    Status = models.CharField(max_length = 100)
    Excepted_day_of_delivery = models.DateField()
    Id_delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE,null =True)

    class Meta:
        verbose_name = "History_transaction"
        verbose_name_plural = "History_transactions"


