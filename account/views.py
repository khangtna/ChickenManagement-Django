from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, decorators

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets

import requests

# Create your views here.


def getAllAccount(request):

    context= {}
    url_api= requests.get('https://apichicken.herokuapp.com/api/account/')
    context = url_api.json()

    return render(request, 'homepage/account/account.html', {
        'account': context
        })


def login(request):
    
    return render(request, 'homepage/login.html')



def addAcc(request):
    return render(request, 'homepage/account/addACC.html')


