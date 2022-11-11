from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, decorators

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets

import requests
from .forms import AccountPostForm


# Create your views here.


def login(request):

    url_api_account= requests.get('https://apichicken.herokuapp.com/api/account/')
    account = url_api_account.json()

    admin= account[0]
    print(admin['name_account'])
    print(admin['password'])
    

    form= AccountPostForm(request.POST or None)
    if form.is_valid():
        form.save()

    username_ = form.data.get('username')
    # print(username_)
    password_ = form.data.get('pasword')
    # print(password_)
    
    return render(request, 'homepage/login.html')


def getAllAccount(request):

    context= {}
    url_api= requests.get('https://apichicken.herokuapp.com/api/account/')
    context = url_api.json()

    return render(request, 'homepage/account/account.html', {
        'account': context
        })





def addAcc(request):
    return render(request, 'homepage/account/addACC.html')


