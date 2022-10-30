from django.urls import path, include

from rest_framework import routers

from . import views

app_name= 'emp'

urlpatterns = [

    path('', views.api_getAllEmp, name='emp'),
    path('<id>/', views.api_getIDEmp, name='empID'),


]
