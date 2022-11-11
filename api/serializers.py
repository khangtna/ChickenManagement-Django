from rest_framework import serializers

from emp.models import EMPs
from product.models import Products, Category
from account.models import Account


class EMPSerializer(serializers.ModelSerializer):

    class Meta:
        model= EMPs
        fields = ('id', 'l_name', 'f_name', 'gender', 'date','numberPhone','address', 'salary','status' )


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

        extra_kwargs= {
        'password': {'write_only': 'true'}

        }

    def create(self, validated_data):
        user= Account(**validated_data)
        user.set_password(user.password)
        user.save()

        return user


