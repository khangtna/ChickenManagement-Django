from argparse import Action
from urllib import response
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages

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
    url_api= requests.get('https://apichicken.herokuapp.com/api/emp/')
    context = url_api.json()

    return render(request, 'homepage/emp/EMP.html', {
        'emps': context
        })


def addEMP(request):

    url_api_account= requests.get('https://apichicken.herokuapp.com/api/account/')
    account_ = url_api_account.json()

    url_api= 'https://apichicken.herokuapp.com/api/emp/'
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
    data['id_account']= form.data.get('account')
    data['status']= form.data.get('status')
  
    # print(data)


    requests.post(url_api, data=data)


    
    return render(request, 'homepage/emp/addEMP.html', {

        'account':account_

    })


def delEMP(request, id):

    url_api= 'https://apichicken.herokuapp.com/api/emp/%s' %id
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
    data['id_account']= form.data.get('account')
    data['status']= form.data.get('status')

    # print(data)
    
    requests.delete(url_api, data=data)

    return redirect('/emp')



def updateEMP(request, id):

    url_api_account= requests.get('https://apichicken.herokuapp.com/api/account/')
    account_ = url_api_account.json()

    url_api= 'https://apichicken.herokuapp.com/api/update/%s/' %id
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
    data['id_account']= form.data.get('account')
    data['status']= form.data.get('status')

    print(data)
    
    requests.put(url_api, data=data)

    return render(request, 'homepage/emp/updateEMP.html', {

        'emp': context,
        'account': account_
        
        })



