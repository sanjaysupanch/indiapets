from accounts.models import CustomUser
from .models import *
from rest_framework import serializers
from seller.models import *


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model=seller
        fields= ['id', 'pet_type', 'pet_name', 'pet_breed', 'pet_image', 'pet_gender', 'is_verified', 'doctor_reg_no', 'doctor_name',]
        read_only_fields=('id','pet_type','pet_name', 'pet_breed', 'pet_image', 'pet_gender')




