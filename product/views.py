from argparse import Action
from urllib import response
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets

import requests
import json
# Create your views here.

def home(request):
    return render(request, 'homepage/product/addProduct.html')


def getAllProduct(request):

    url_api= requests.get('https://apichicken.herokuapp.com/api/product/')
    context = url_api.json()

    return render(request, 'homepage/product/Products.html', {
        'product': context
        })

