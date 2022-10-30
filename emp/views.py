from argparse import Action
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets


from .models import EMPs



# Create your views here.


def getAllEMP(request):

    context = {}
    # emp = get_object_or_404(EMPs, pk = 'id') # dùng khi có điều kiện
    emp = EMPs.objects.all()

    context['emps']= emp

    return render(request, 'homepage/tables.html', context)




