from django.urls import path, include

from rest_framework import routers

from . import views


urlpatterns = [

    path('', views.getAllOrder, name='order'),
    # path('add/', views.addProduct, name='addproduct'),
    # path('del/<id>', views.delProduct, name='delproduct'),
    # path('edit/<id>', views.editProduct, name='editproduct'),

    path('<email>', views.userHome, name='info-user'),
    path('<email>/add', views.addOrder, name='addorder'),
    path('<email>/<id>/orderdetail', views.Orderdetail, name='order-orderdetail'),
   
    
]
