from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Catagory(models.Model):
    name = models.CharField(max_length=150,blank=False)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    catagory = models.ForeignKey(Catagory,null=True,blank=False,on_delete=models.SET_NULL)
    pname = models.CharField(max_length=100,blank=False)
    brand = models.CharField(max_length=100,null=True,blank=False) 
    price = models.DecimalField(decimal_places=2,max_digits=10)
    
    
    desc = models.TextField(default="",blank=False)
    image = models.ImageField(upload_to="static/images")
    
    def __str__(self):
       return self.pname
    
class CartItem(models.Model):
    product = models.ForeignKey(Product,null=True,blank=True,on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(null=True,blank=True)

     


