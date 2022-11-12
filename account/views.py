from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, decorators
from django.contrib.auth import login as auth_login
from django.contrib import messages

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets

import requests
from .forms import AccountPostForm
import json


# Create your views here.

def loginHome(request):
    return render(request, 'homepage/login.html')

def login(request):

    # url_api_permission= requests.get('https://apichicken.herokuapp.com/api/permission/')
    # permission_ = url_api_permission.json()

    # url_api_account= requests.get('https://apichicken.herokuapp.com/api/account/')
    # account_ = url_api_account.json()



    url_api_account= 'http://127.0.0.1:8000/api/login/'

    data={}
    context={}

    if request.method == 'POST':
        username_= request.POST.get('username')
        password_= request.POST.get('password')


        data['username']= username_
        data['password']= password_

        a= requests.post(url_api_account, data=data)
        b= a.json()
        
        
        # print(b)
        
        user = authenticate(request, username= username_, password= password_)
        auth_login(request, user)

        if 'non_field_errors' in b:
            messages.error(request, 'Tài khoản hoặc mật khẩu không đúng!')
            return redirect('/')
        

        if b['username']== 'admin':

            # context['email']= b['email']
            return redirect('/emp')
            
        else:
            # context['email']= b['email']
            return redirect('/user')
    
    
    return render(request, 'homepage/login.html',{
        "email": context
    })


def logoutUser(request):
    logout(request)
    return redirect('/')



# account
def getAllAccount(request):

    context= {}
    url_api= requests.get('https://apichicken.herokuapp.com/api/user/')
    # print(type(url_api))
    context = url_api.json()
    # print(type(context))

    return render(request, 'homepage/account/account.html', {
        'account': context
        })



def addAcc(request):

    url_api_add= 'https://apichicken.herokuapp.com/api/user/'
    data={}     
    
    form= AccountPostForm(request.POST or None)
    if form.is_valid():
        form.save()

    data['username']= form.data.get('tenDN')
    data['password']= form.data.get('matKhau')
    data['email']= form.data.get('email')
  
    # print(data)
    
    requests.post(url_api_add, data=data)

    return render(request, 'homepage/account/addACC.html')


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


def getAllPermission(request):

    context= {}
    url_api= requests.get('https://apichicken.herokuapp.com/api/permission/')
    context = url_api.json()

    return render(request, 'homepage/account/permission.html', {
        'permission': context
        })


def addPer(request):

    url_api_add= 'https://apichicken.herokuapp.com/api/permission/'
    data={}     
    
    form= AccountPostForm(request.POST or None)
    if form.is_valid():
        form.save()

    data['name_per']= form.data.get('nameper')
  
    # print(data)
    
    requests.post(url_api_add, data=data)

    return render(request, 'homepage/account/addPer.html')


def editPer(request, id):

    url_api_edit= 'https://apichicken.herokuapp.com/api/permission/%s/' %id

    url_api_per= requests.get(url_api_edit)
    per = url_api_per.json()

    data={}     

    form= AccountPostForm(request.POST or None)
    if form.is_valid():
        form.save()

    data['name_per']= form.data.get('nameper')

    print(data)
    
    # requests.put(url_api_edit, data=data)
    requests.patch(url_api_edit, data=data)

    return render(request, 'homepage/account/editPer.html', {

        'per': per
        
        })



