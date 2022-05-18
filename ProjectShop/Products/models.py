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