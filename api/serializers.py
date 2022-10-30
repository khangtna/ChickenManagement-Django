from rest_framework import serializers
from emp import models

class EMPSerializer(serializers.ModelSerializer):

    class Meta:
        model= models.EMPs
        fields = ('id', 'l_name', 'f_name', 'gender', 'date','numberPhone','address', 'salary','status' )


