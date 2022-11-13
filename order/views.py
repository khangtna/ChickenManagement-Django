from argparse import Action
from urllib import response
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets

from .forms import CreateOrderdetailPostForm

import requests
import json

# Create your views here.


def userHome(request, email):

    url_api= 'https://apichicken.herokuapp.com/api/infouser/%s' %email

    emp_= requests.get(url_api)
    emp= emp_.json()

    url_api_order= 'https://apichicken.herokuapp.com/api/order/'

    order_= requests.get(url_api_order)
    order= order_.json()


    return render(request, 'homepage/order/Order.html', {
        'emp': emp,
        'order':order
    })


def getAllOrder(request):

    context= {}
    url_api= requests.get('https://apichicken.herokuapp.com/api/order/')
    # print(type(url_api))
    context = url_api.json()
    # print(type(context))

    return render(request, 'homepage/order/Oder.html', {
        'account': context
        })



def addOrder(request, email):

    url_api= 'https://apichicken.herokuapp.com/api/infouser/%s' %email

    emp_= requests.get(url_api)
    emp= emp_.json()

    url_api_order= 'https://apichicken.herokuapp.com/api/order/'

    data={}     

    data['id_emp']= emp['id']

    # print(data)
    
    requests.post(url_api_order, data=data)

    return redirect('info-user', email=email)


#oderdetail
def Orderdetail(request, email, id):

    url_api_emp= 'https://apichicken.herokuapp.com/api/infouser/%s' %email
    emp_= requests.get(url_api_emp)
    emp= emp_.json()


    url_api_product= 'https://apichicken.herokuapp.com/api/product/' 
    product_= requests.get(url_api_product)
    product= product_.json()


    url_api_order= 'https://apichicken.herokuapp.com/api/order/%s' %id
    order_= requests.get(url_api_order)
    order= order_.json()


    url_api_orderdetail= 'https://apichicken.herokuapp.com/api/order/%s/orderdetail/' %id

    orderdetail_= requests.get(url_api_orderdetail)
    orderdetail= orderdetail_.json()


    url_api= 'https://apichicken.herokuapp.com/api/orderdetail/'
    
    data={}     

    form= CreateOrderdetailPostForm(request.POST or None)
    if form.is_valid():
        form.save()

    data['id_Order']= order['id_Order']
    data['id_Product']= form.data.get('maMonAn')
    data['quantity']= form.data.get('quantity')

    data1= {}


    
    # requests.post(url_api, data=data)
    # requests.post(url_api_order, data=data1)

    return render(request, 'homepage/order/Orderdetail.html', {

        'emp': emp,
        'product': product,
        'order': order,
        'orderdetail':orderdetail


        })


def addOrderdetail(request, email, id):

    url_api_emp= 'https://apichicken.herokuapp.com/api/infouser/%s' %email
    emp_= requests.get(url_api_emp)
    emp= emp_.json()


    url_api_product= 'https://apichicken.herokuapp.com/api/product/' 
    product_= requests.get(url_api_product)
    product= product_.json()


    url_api_order= 'https://apichicken.herokuapp.com/api/order/%s' %id
    order_= requests.get(url_api_order)
    order= order_.json()


    url_api_orderdetail= 'https://apichicken.herokuapp.com/order/%s/orderdetail/' %id

    orderdetail_= requests.get(url_api_orderdetail)
    orderdetail= orderdetail_.json()


    url_api= 'https://apichicken.herokuapp.com/api/orderdetail/'
    
    data={}     

    form= CreateOrderdetailPostForm(request.POST or None)
    if form.is_valid():
        form.save()

    data['id_Order']= form.data.get('maHD')
    data['id_Product']= form.data.get('maMonAn')
    data['quantity']= form.data.get('quantity')


    
    requests.post(url_api, data=data)
    # requests.post(url_api_order, data=data1)

    return render(request, 'homepage/order/addOrderdetail.html', {

        'emp': emp,
        'product': product,
        'order': order,
        'orderdetail':orderdetail


        })



def delOrderdetail(request, email,id, idorder):

    url_api= 'https://apichicken.herokuapp.com/api/infouser/%s' %email

    emp_= requests.get(url_api)
    emp= emp_.json()

    url_api_orderdetail= 'https://apichicken.herokuapp.com/api/orderdetail/%s' %id

    data={}     

    # data['id_orderdetail']= 

    # print(data)
    
    requests.delete(url_api_orderdetail, data=data)

    return redirect('order-orderdetail', email=email, id= idorder)


