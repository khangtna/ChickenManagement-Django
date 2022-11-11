from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, decorators

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets

import requests
from .forms import AccountPostForm


# Create your views here.

def loginHome(request):
    return render(request, 'homepage/login.html')

def login(request):

    url_api_account= requests.get('https://apichicken.herokuapp.com/api/permission/')
    permission_ = url_api_account.json()

    admin= permission_[0]
    print(admin)
    # username = admin['name_account']
    # password = admin['password']
    

    form= AccountPostForm(request.POST or None)
    if form.is_valid():
        form.save()

    username_ = form.data.get('username')
    password_ = form.data.get('pasword')

    # admin
    # if username_ == username and password_ == password:
    #     return redirect('/emp')
    
    
    return render(request, 'homepage/login.html')


# account

def getAllAccount(request):

    context= {}
    url_api= requests.get('https://apichicken.herokuapp.com/api/account/')
    context = url_api.json()

    return render(request, 'homepage/account/account.html', {
        'account': context
        })



def addAcc(request):

    url_api_per= requests.get('https://apichicken.herokuapp.com/api/permission/')
    per = url_api_per.json()

    url_api_add= 'https://apichicken.herokuapp.com/api/account/'
    data={}     
    
    form= AccountPostForm(request.POST or None)
    if form.is_valid():
        form.save()

    data['name_account']= form.data.get('tenDN')
    data['password']= form.data.get('matKhau')
    data['id_per']= form.data.get('per')
  
    # print(data)
    
    requests.post(url_api_add, data=data)

    return render(request, 'homepage/account/addACC.html',{
        'per': per
    })


def delAcc(request, id):

    url_api= 'https://apichicken.herokuapp.com/api/account/%s' %id

    data={}     

    form= AccountPostForm(request.POST or None)
    if form.is_valid():
        form.save()

    data['name_account']= form.data.get('tenDN')
    data['password']= form.data.get('matKhau')
    data['id_per']= form.data.get('per')

    # print(data)
    
    requests.delete(url_api, data=data)

    return redirect('/account')



def editAcc(request, id):

    url_api_edit= 'https://apichicken.herokuapp.com/api/account/%s/' %id

    # url_api= 'https://apichicken.herokuapp.com/api/account/%s/' %id

    url_api_per= requests.get('https://apichicken.herokuapp.com/api/permission/')
    per = url_api_per.json()

    url_api_get= requests.get(url_api_edit)
    context = url_api_get.json()

    data={}     

    form= AccountPostForm(request.POST or None)
    if form.is_valid():
        form.save()

    data['name_account']= form.data.get('tenDN')
    data['password']= form.data.get('matKhau')
    data['id_per']= form.data.get('per')

    print(data)
    
    # requests.put(url_api_edit, data=data)
    requests.patch(url_api_edit, data=data)

    return render(request, 'homepage/account/editACC.html', {

        'per': per,
        'acc': context
        
        })

