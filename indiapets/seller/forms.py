from django import forms
# from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *



class sellerForm(forms.ModelForm):

    class Meta:
        model=seller
        fields=['pet_name', 'pet_breed',  'pet_image', 'pet_age', 'pet_gender', 'pet_price', 'pet_description']

 