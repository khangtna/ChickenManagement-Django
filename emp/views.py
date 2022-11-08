from argparse import Action
from urllib import response
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets

import requests
import json
from types import SimpleNamespace

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
    
    form= CreateEMPPostForm(request.POST or None)
    if form.is_valid():
        form.save()

    data['l_name']= form.data.get('l_name')
    data['f_name']= form.data.get('f_name')
    data['gender']= form.data.get('gender')
    data['date']= form.data.get('date')
    data['address']= form.data.get('address')
    data['numberPhone']= form.data.get('numberPhone')
    data['salary']= form.data.get('salary')
    data['status']= form.data.get('status')
  
    # print(data)
    
    requests.post(url_api, data=data)
    
    return render(request, 'homepage/addEMP.html')


def delEMP(request, id):

    url_api= 'https://apichicken.herokuapp.com/api/emp/abc/%s' %id
    # url_api= 'https://apichicken.herokuapp.com/api/delete/%s' %id
    # context = url_api.json()
    data={}     

    form= CreateEMPPostForm(request.POST or None)
    if form.is_valid():
        form.save()

    data['l_name']= form.data.get('l_name')
    data['f_name']= form.data.get('f_name')
    data['gender']= form.data.get('gender')
    data['date']= form.data.get('date')
    data['address']= form.data.get('address')
    data['numberPhone']= form.data.get('numberPhone')
    data['salary']= form.data.get('salary')
    data['status']= form.data.get('status')

    # print(data)
    
    requests.delete(url_api, data=data)

    return redirect('/emp')



def updateEMP(request, id):

    # url_api= 'https://apichicken.herokuapp.com/api/emp/abc/%s' %id
    url_api= 'https://apichicken.herokuapp.com/api/update/%s' %id
    url_get='https://apichicken.herokuapp.com/api/%s/' %id

    info_emp= requests.get(url_get)
    context = info_emp.json()

    data={}     

    form= CreateEMPPostForm(request.POST or None )
    if form.is_valid():
        form.save()

    data['l_name']= form.data.get('l_name')
    data['f_name']= form.data.get('f_name')
    data['gender']= form.data.get('gender')
    data['date']= form.data.get('date')
    data['address']= form.data.get('address')
    data['numberPhone']= form.data.get('numberPhone')
    data['salary']= form.data.get('salary')
    data['status']= form.data.get('status')

    print(data)
    
    requests.put(url_api, data=data)

    return render(request, 'homepage/updateEMP.html', {

        'emp': context
        
        })



