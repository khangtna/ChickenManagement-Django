from django.urls import path, include

from rest_framework import routers

from . import views


urlpatterns = [

    path('', views.getAllProduct, name='product'),
    path('add/', views.addProduct, name='addproduct'),
    # path('del/<id>', views.delEMP, name='delemp'),
    # path('update/<id>', views.updateEMP, name='updateemp'),
   

    
]
