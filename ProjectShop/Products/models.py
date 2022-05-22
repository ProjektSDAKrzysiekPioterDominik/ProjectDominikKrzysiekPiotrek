from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Client(models.Model):
    Login = models.TextField(max_length = 20)
    Name = models.TextField(max_length = 20)
    Surname = models.TextField(max_length = 20)
    Adress = models.TextField(max_length = 100)
    Email = models.TextField(max_length = 20)
    Phone = models.TextField(max_length = 20)
    Birth_date = models.DateField()
    City = models.TextField(max_length = 20)


class Products(models.Model):
    Id_category = models.IntegerField()
    Product_name = models.CharField(max_length=100)
    Price = models.DecimalField(default=0,validators=[MinValueValidator(0.01)], max_digits=12, decimal_places=2)
    Image = models.ImageField(blank=True)
    Describe = models.TextField(max_length=500)
    Date_added = models.DateField()
    Is_listed = models.BooleanField()
    #Id_client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Product_name} - {self.Price} - {self.Is_listed} - {self.Image}"



class Categories(models.Model):
    Name = models.CharField(max_length = 100)


class Basket(models.Model):
    Id_product = models.IntegerField()
    Id_client = models.IntegerField()
    Quantity = models.IntegerField()
    Price = models.DecimalField(max_digits = 12, decimal_places = 2)


class History_transactions(models.Model):
    Id_client = models.IntegerField()
    Date_of_buy = models.DateField()
    Price = models.DecimalField(max_digits = 12, decimal_places = 2)
    Status = models.CharField(max_length = 100)
    Excepted_day_of_delivery = models.DateField()
    Id_delivery = models.IntegerField()

class Delivery(models.Model):
    Name = models.TextField(max_length = 1000)
    Surname = models.TextField(max_length = 1000)
    Company_name = models.TextField(max_length = 1000)
    Phone = models.TextField(max_length = 1000)
    Email = models.TextField(max_length = 1000)

