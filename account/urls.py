from django.urls import path, include

from rest_framework import routers

from . import views

urlpatterns = [

    path('', views.getAllAccount, name='account'),
    path('add/', views.addAcc, name='addacc'),
    # path('del/<id>', views.delEMP, name='delemp'),
    # path('update/<id>', views.updateEMP, name='updateemp'),
   
    # path('login/', views.login, name='login'),

    
]
