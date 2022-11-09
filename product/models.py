from django.db import models

from emp.models import EMPs


# Create your models here.


class Category(models.Model):

    id_category = models.AutoField(primary_key=True)
    name_category = models.CharField(max_length= 15)
    
    def __str__(self):
        return str(self.id_category)


class Products(models.Model):

    id_product = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 15)
    id_category= models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField(default= 0)
    status= models.BooleanField(default= True)

    def __str__(self):
        return str(self.id_product)




