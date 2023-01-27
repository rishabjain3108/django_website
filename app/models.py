from django.db import models
from django.contrib.auth.models import User

class contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=30)
    message = models.CharField(max_length=100)

class information(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=30)
    address =  models.CharField(max_length=30)
ITEM_CHOICES = (
    ('ring','ring'),
    ('earrings','earrings'),
    ('sets','sets'),
    ('hairaccessories','hairaccessories'),
)
class items(models.Model):
    name = models.CharField(max_length=15)
    price = models.IntegerField()
    desc = models.CharField(max_length=150)
    image = models.ImageField(upload_to='static/new',null=True,blank=True)
    type = models.CharField(choices=ITEM_CHOICES,max_length=20)     

class Cart(models.Model):
        quantity  = models.PositiveIntegerField(default=1)
        user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
        items = models.ForeignKey(items,on_delete=models.CASCADE,blank=True,null=True)
       


    
    







