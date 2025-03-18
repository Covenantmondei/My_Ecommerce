from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Store(models.Model):
    store_name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255, blank=True)
    owner_name = models.CharField(max_length=50)
    password = models.CharField(max_length=20, unique=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.store_name

class Product(models.Model):
    Product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    product_key = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="products", null=True, blank=True)
    
    def __str__(self):
        return self.Product_name