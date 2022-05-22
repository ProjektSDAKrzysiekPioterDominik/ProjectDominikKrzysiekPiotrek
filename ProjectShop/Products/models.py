from django.db import models

# Create your models here.
class Products(models.Model):
    Id = models.IntegerField()
    Date_added = models.DateField()
    Is_listed = models.BooleanField()
    Describe = models.TextField(max_length = 1000)
    Image = models.ImageField()
    Price = models.DecimalField(max_digits = 12, decimal_places = 2)
    Product_name = models.CharField(max_length = 100)
    Id_category = models.IntegerField()
    Id_client = models.IntegerField()

class Categories(models.Model):
    Id = models.IntegerField()
    Name = models.CharField(max_length = 100)

class Client(models.Model):
    Id = models.IntegerField()
    Login = models.TextField(max_length = 1000)
    Name = models.TextField(max_length = 1000)
    Surname = models.TextField(max_length = 1000)
    Adress = models.TextField(max_length = 1000)
    Email = models.TextField(max_length = 1000)
    Phone = models.TextField(max_length = 1000)
    Birth_date = models.DateField()
    City = models.TextField(max_length = 1000)

class Basket(models.Model):
    Id = models.IntegerField()
    Id_product = models.IntegerField()
    Id_client = models.IntegerField()
    Quantity = models.IntegerField()
    Price = models.DecimalField(max_digits = 12, decimal_places = 2)


class History_transactions(models.Model):
    Id = models.IntegerField()
    Id_client = models.IntegerField()
    Date_of_buy = models.DateField()
    Price = models.DecimalField(max_digits = 12, decimal_places = 2)
    Status = models.CharField(max_length = 100)
    Excepted_day_of_delivery = models.DateField()
    Id_delivery = models.IntegerField()

class Delivery(models.Model):
    Id = models.IntegerField()
    Name = models.TextField(max_length = 1000)
    Surname = models.TextField(max_length = 1000)
    Company_name = models.TextField(max_length = 1000)
    Phone = models.TextField(max_length = 1000)
    Email = models.TextField(max_length = 1000)
