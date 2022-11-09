from django.db import models

# Create your models here.

class Permission(models.Model):

    id_per = models.AutoField(primary_key=True)
    name_per = models.CharField(max_length= 15)
    
    def __str__(self):
        return str(self.id_per)


class Account(models.Model):

    id_account = models.AutoField(primary_key=True)
    name_account = models.CharField(max_length= 15)
    id_per= models.ForeignKey(Permission, on_delete=models.CASCADE)
    # status= models.BooleanField(default= True)

    def __str__(self):
        return str(self.id_account)

