from django.urls import path, include

from rest_framework import routers

from . import views

urlpatterns = [

    path('', views.getAllAccount, name='account'),
    path('add/', views.addAcc, name='addacc'),
    path('del/<id>', views.delAcc, name='delacc'),
    # path('update/<id>', views.editAcc, name='editacc'),
   
    # path('login/', views.login, name='login'),

    # path('permission/', views.getAllPermission, name='permission'),
    # path('permission/add/', views.addPer, name='addper'),
    # path('permission/update/<id>', views.editPer, name='editper'),

    # path('info/<email>', views.userHome, name='info-user'),

    
]
