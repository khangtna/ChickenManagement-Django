from django.contrib import admin

from .models import Account, Permission

# Register your models here.


admin.site.register(Account)
admin.site.register(Permission)
