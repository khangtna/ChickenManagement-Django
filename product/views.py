from argparse import Action
from urllib import response
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets

from .forms import CreateProductPostForm

import requests
import json
# Create your views here.



def getAllProduct(request):

    context= {}
    url_api= requests.get('https://apichicken.herokuapp.com/api/product/')
    context = url_api.json()

    return render(request, 'homepage/product/Products.html', {
        'product': context
        })


def addProduct(request):

    url_api= 'https://apichicken.herokuapp.com/api/product/'
    # url_api_category= 'https://apichicken.herokuapp.com/api/category/'
    # context = url_api.json()
    data={}     
    
    form= CreateProductPostForm(request.POST or None)
    if form.is_valid():
        form.save()

    data['name']= form.data.get('tenMonAn')
    data['price']= form.data.get('giaMonAn')
    data['price']= form.data.get('giaMonAn')
    data['status']= form.data.get('status')
  
    print(data)
    
    requests.post(url_api, data=data)

    return render(request, 'homepage/product/addProduct.html')


