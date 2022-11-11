from django.urls import path, include

from rest_framework import routers

from . import views


urlpatterns = [

    path('', views.getAllProduct, name='product'),
    path('add/', views.addProduct, name='addproduct'),
    path('del/<id>', views.delProduct, name='delproduct'),
    path('edit/<id>', views.editProduct, name='editproduct'),
   
    path('category/', views.getAllCategory, name='category'),
    path('category/add/', views.addCategory, name='addcategory'),
    path('category/del/<id>', views.delCategory, name='delcategory'),
    path('category/edit/<id>', views.editCategory, name='editcategory'),

    
]
