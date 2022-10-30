from argparse import Action
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status, permissions, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from emp.models import EMPs

from .serializers import EMPSerializer


@api_view(['GET', ])
def api_getAllEmp(request):
    
    try:
        emps = EMPs.objects.filter(status = True)

    except EMPs.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serilaizer = EMPSerializer(emps, many= True)
        return Response(serilaizer.data)


@api_view(['GET', ])
def api_getIDEmp(request,id):
    
    try:
        emps = EMPs.objects.get(id = id)

    except EMPs.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serilaizer = EMPSerializer(emps)
        return Response(serilaizer.data)


@api_view(['PUT', ])
def api_updateEmp(request, id):
    
    try:
        emps = EMPs.objects.get(id = id)

    except EMPs.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serilaizer = EMPSerializer(emps, data= request.data)
        data={}
        if serilaizer.is_valid():
            serilaizer.save()
            data['success']= 'Cập nhật thành công!'
            return Response(data= data)

        return Response(serilaizer.errors, status= status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE', ])
def api_updateEmp(request, id):
    
    try:
        emps = EMPs.objects.get(id = id)

    except EMPs.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        delemp= emps.delete()
        data={}

        if delemp:
            data['success']= 'Xóa thành công!'
        else: 
            data['fail']= 'Xóa thất bại!'
            

        return Response(data= data)





