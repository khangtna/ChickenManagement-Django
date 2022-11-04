from argparse import Action
from urllib import response
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets

import requests
import json

from .models import EMPs
from .forms import CreateEMPPostForm



# Create your views here.


def getAllEMP(request):

    # context = {}
    # emp = get_object_or_404(EMPs, pk = 'id') # dùng khi có điều kiện
    # emp = EMPs.objects.all()

    # context['emps']= emp
    url_api= requests.get('https://apichicken.herokuapp.com/api/emp/abc/')
    context = url_api.json()

    return render(request, 'homepage/EMP.html', {
        'emps': context
        })


def addEMP(request):

    url_api= 'https://apichicken.herokuapp.com/api/emp/abc/'
    # context = url_api.json()
    data={}

    # if request.method== "POST":
    #     l_name= request.GET['l_name']
    #     f_name= request.GET['f_name']
    #     gender= request.GET['gt']
    #     date= request.GET['date']
    #     address= request.GET['address']
    #     numberPHone= request.GET['numberPhone']
    #     salary= request.GET['salary']

    #     data['l_name']= l_name
    #     data['f_name']= f_name
    #     data['gender']= gender
    #     data['date']= date
    #     data['address']= address
    #     data['numberPhone']= numberPhone
    #     data['salary']= salary

        

    form= CreateEMPPostForm(request.POST or None)
    if form.is_valid():
        form.save()



    data['l_name']= form.data['l_name']
    data['f_name']= form.data['f_name']
    data['gender']= form.data.get('gender')
    data['date']= form.data['date']
    data['address']= form.data['address']
    data['numberPhone']= form.data['numberPhone']
    data['salary']= form.data['salary']
  

    print(data)
    
    requests.post(url_api, data=data)

    return render(request, 'homepage/addEMP.html')

