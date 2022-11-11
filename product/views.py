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

    url_api_category= requests.get('https://apichicken.herokuapp.com/api/category/')
    context = url_api_category.json()

    # url_api= 'https://apichicken.herokuapp.com/api/product/'
    url_api_add= 'https://apichicken.herokuapp.com/api/product/add/'
    data={}     
    
    form= CreateProductPostForm(request.POST or None)
    if form.is_valid():
        form.save()

    data['name']= form.data.get('tenMonAn')
    data['id_category']= form.data.get('category')
    data['price']= form.data.get('giaMonAn')
    data['status']= form.data.get('status')
  
    # print(data)
    
    requests.post(url_api_add, data=data)

    return render(request, 'homepage/product/addProduct.html', {
        "category": context

    })


def delProduct(request, id):

    url_api= 'https://apichicken.herokuapp.com/api/product/%s' %id

    data={}     

    form= CreateProductPostForm(request.POST or None)
    if form.is_valid():
        form.save()

    data['name']= form.data.get('tenMonAn')
    data['id_category']= form.data.get('category')
    data['price']= form.data.get('giaMonAn')
    data['status']= form.data.get('status')

    # print(data)
    
    requests.delete(url_api, data=data)

    return redirect('/product')


def editProduct(request, id):

    # url_api_edit= 'https://apichicken.herokuapp.com/api/product/edit/%s/' %id
    url_api_edit= 'https://apichicken.herokuapp.com/api/product/%s/' %id

    url_api= 'https://apichicken.herokuapp.com/api/product/%s/' %id

    url_api_category= requests.get('https://apichicken.herokuapp.com/api/category/')
    category = url_api_category.json()

    info_emp= requests.get(url_api)
    context = info_emp.json()

    data={}     

    form= CreateProductPostForm(request.POST or None)
    if form.is_valid():
        form.save()

    data['name']= form.data.get('tenMonAn')
    data['id_category']= form.data.get('category')
    data['price']= form.data.get('giaMonAn')
    data['status']= form.data.get('status')

    print(data)
    
    # requests.put(url_api_edit, data=data)
    requests.patch(url_api_edit, data=data)

    return render(request, 'homepage/product/editProduct.html', {

        'product': context,
        'category': category
        
        })


# Category

def getAllCategory(request):

    context= {}
    url_api= requests.get('https://apichicken.herokuapp.com/api/category/')
    context = url_api.json()

    return render(request, 'homepage/product/Category.html', {
        'category': context
        })


def addCategory(request):

    url_api_add= 'https://apichicken.herokuapp.com/api/category/'
    data={}     
    
    form= CreateProductPostForm(request.POST or None)
    if form.is_valid():
        form.save()

    data['name_category']= form.data.get('tenDM')
  
    # print(data)
    
    requests.post(url_api_add, data=data)

    return render(request, 'homepage/product/addCategory.html')


def delCategory(request, id):

    url_api= 'https://apichicken.herokuapp.com/api/category/%s' %id

    data={}     

    form= CreateProductPostForm(request.POST or None)
    if form.is_valid():
        form.save()

    data['id_category']= form.data.get('tenDN')

    # print(data)
    
    requests.delete(url_api, data=data)

    return redirect('/product/category')


def editCategory(request, id):

    # url_api_edit= 'https://apichicken.herokuapp.com/api/product/edit/%s/' %id
    # url_api_edit= 'https://apichicken.herokuapp.com/api/category/%s/' %id

    url_api= 'https://apichicken.herokuapp.com/api/category/%s/' %id


    info= requests.get(url_api)
    context = info.json()

    data={}     

    form= CreateProductPostForm(request.POST or None)
    if form.is_valid():
        form.save()

    data['name_category']= form.data.get('tenDM')

    print(data)
    
    # requests.put(url_api_edit, data=data)
    requests.patch(url_api, data=data)

    return render(request, 'homepage/product/editCategory.html', {
        'category': context
        
        })


