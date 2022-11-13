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


def userHome(request, email):

    url_api= 'http://127.0.0.1:8000/api/infouser/%s' %email

    emp_= requests.get(url_api)
    emp= emp_.json()

    url_api_order= 'http://127.0.0.1:8000/api/order/'

    order_= requests.get(url_api_order)
    order= order_.json()


    return render(request, 'homepage/order/Order.html', {
        'emp': emp,
        'order':order
    })


def getAllOrder(request):

    context= {}
    url_api= requests.get('http://127.0.0.1:8000/api/order/')
    # print(type(url_api))
    context = url_api.json()
    # print(type(context))

    return render(request, 'homepage/order/Oder.html', {
        'account': context
        })



def addOrder(request, email):

    url_api= 'http://127.0.0.1:8000/api/infouser/%s' %email

    emp_= requests.get(url_api)
    emp= emp_.json()

    url_api_order= 'http://127.0.0.1:8000/api/order/'

    data={}     

    data['id_emp']= emp['id']

    # print(data)
    
    requests.post(url_api_order, data=data)

    return redirect('info-user', email=email)



def Orderdetail(request, email, id):

    url_api_emp= 'http://127.0.0.1:8000/api/infouser/%s' %email
    emp_= requests.get(url_api_emp)
    emp= emp_.json()


    url_api_product= 'http://127.0.0.1:8000/api/product/' 
    product_= requests.get(url_api_product)
    product= product_.json()


    url_api_order= 'http://127.0.0.1:8000/api/order/%s' %id
    order_= requests.get(url_api_order)
    order= order_.json()


    url_api_orderdetail= 'http://127.0.0.1:8000/api/order/%s/orderdetail/' %id

    orderdetail_= requests.get(url_api_orderdetail)
    orderdetail= orderdetail_.json()


    url_api= 'http://127.0.0.1:8000/api/orderdetail/'
    
    data={}     

    data['id_Order']= order['id_Order']
    data['id_Product']= request.POST.get('maMonAn')
    data['quantity']= request.POST.get('quantity')

    data1= {}

    


    print(data)
    
    requests.post(url_api, data=data)
    requests.post(url_api_order, data=data1)

    return render(request, 'homepage/order/Orderdetail.html', {

        'emp': emp,
        'product': product,
        'order': order,
        'orderdetail':orderdetail


        })



