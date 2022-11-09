from rest_framework import serializers

from emp import models
from product import models


class EMPSerializer(serializers.ModelSerializer):

    class Meta:
        model= models.EMPs
        fields = ('id', 'l_name', 'f_name', 'gender', 'date','numberPhone','address', 'salary','status' )


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model= models.Product
        fields = ('id_product', 'name', 'category', 'price','status' )


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model= models.Category
        fields = ('id_category', 'name_category')

