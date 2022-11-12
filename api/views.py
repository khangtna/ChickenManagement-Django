from argparse import Action
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login 


from rest_framework import status, permissions, viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken

from emp.models import EMPs
from product.models import Products, Category
from account.models import Account, Permission

from .serializers import (

    EMPSerializer, 
    ProductSerializer, 
    CategorySerializer, 
    AccountSerializer,
    PermissionSerializer,
    UserSerializer,
    RegisterSerializer

)


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
def api_delEmp(request, id):
    
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


@api_view(['POST', ])
# @permission_classes([permissions.AllowAny])
def api_createEmp(request):
    
    if request.method == 'POST':
        
        serilaizer = EMPSerializer(data= request.data)

        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data, status= status.HTTP_201_CREATED)

        return Response(serilaizer.errors, status= status.HTTP_400_BAD_REQUEST)


class apiEMP(viewsets.ModelViewSet):
    queryset = EMPs.objects.filter(status = True)
    serializer_class = EMPSerializer
    permission_classes = [permissions.AllowAny,]
    # permission_classes = [permissions.IsAuthenticated,]
    http_method_names = ['patch','put','get','post','delete' ]


# class apigetEMP(viewsets.ViewSet, generics.ListAPIView):
    
#     serializer_class = EMPSerializer
    
#     def get_queryset(self):
#         emp = EMPs.objects.filter(status = True)

#         id= self.request.query_params.get('id')
#         if id is not None:
#             emp= emp.filter(id__contains=id)
        
#         return emp


class apiProduct(viewsets.ModelViewSet):
    queryset = Products.objects.filter(status = True)
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny,]
    http_method_names = ['patch','put','get','post','delete' ]


class apiCategory(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny,]
    http_method_names = ['patch','put','get','post','delete' ]


class apiAccount(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.AllowAny,]
    http_method_names = ['patch','put','get','post','delete' ]


class apiPermission(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [permissions.AllowAny,]
    http_method_names = ['patch','put','get','post','delete' ]


class apiUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny,]
    http_method_names = ['patch','put','get','post','delete' ]



# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(UserSerializer(user).data)
        # return super(LoginAPI, self).post(request, format=None)



