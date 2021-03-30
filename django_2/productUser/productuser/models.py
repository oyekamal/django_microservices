from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    
class ProductUser(models.Model):
    user_id = models.PositiveIntegerField(default=0)
    product_id = models.PositiveIntegerField(default=0)
    