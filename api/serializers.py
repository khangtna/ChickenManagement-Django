from django.contrib.auth.models import User

from rest_framework import serializers

from emp.models import EMPs
from product.models import Products, Category
from account.models import Account, Permission
from order.models import Order, OrderDetail


class EMPSerializer(serializers.ModelSerializer):

    class Meta:
        model= EMPs
        fields = ('id', 'l_name', 'f_name', 'gender', 'date','numberPhone','address', 'salary','email','status' )


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model= Category
        fields = ('id_category', 'name_category')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model= Products
        fields = ('id_product', 'name', 'id_category', 'price', 'status' )


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model= Account
        fields = ('id_account', 'name_account', 'password' ,'id_per' )

        

class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model= Permission
        fields = ('id_per', 'name_per' )



# class UserSerializer(serializers.ModelSerializer):

#     def create(self, validated_data):
#         user= User(**validated_data)
#         user.set_password(user.password)
#         user.save()

#         return user

#     class Meta:
#         model= User
#         fields = ('id', 'first_name', 'last_name', 'username', 'password', 'email', 'date_joined' )

#         extra_kwargs= {
#         'password': {'write_only': 'true'}

#         }



# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
 

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id_Order', 'id_emp', 'date','status')


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ('id_Order', 'id_Product', 'quantity', 'date_orderdetail')


