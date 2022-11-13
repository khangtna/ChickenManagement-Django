from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from emp.models import EMPs
from product.models import Products

# Create your models here.


class Order(models.Model):

    id_Order = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add= True)
    # sum_price= models.CharField(max_length= 150, default=0)
    id_emp= models.ForeignKey(EMPs, on_delete=models.SET_NULL, blank= True, null=True, related_name="orderemp")
    status= models.BooleanField(default=False)


    def __str__(self):
        return str(self.id_Order)


class OrderDetail(models.Model):

    id_Order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank= True, null=True, related_name="orderdetail")
    id_Product= models.ForeignKey(Products, on_delete=models.SET_NULL, blank= True, null=True)
    quantity = models.IntegerField(default=1)
    # sum_price= models.FloatField(default=0)
    date_orderdetail = models.DateTimeField(auto_now_add= True)
    

    def __str__(self):
        return str(self.id_Order)

    def get_total_price(self):
        return self.quantity * self.id_Product.price



