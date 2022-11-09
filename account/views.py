from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets

import requests

# Create your views here.


def addAcc(request):
    return render(request, 'homepage/account/addACC.html')


