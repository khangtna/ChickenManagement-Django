from django.urls import path, include

from rest_framework import routers

from . import views


urlpatterns = [

    path('', views.getAllProduct, name='product'),
    path('add/', views.addProduct, name='addproduct'),
    path('del/<id>', views.delProduct, name='delproduct'),
    path('edit/<id>', views.editProduct, name='editproduct'),
   

    
]
