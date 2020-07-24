from django.db import models
from django.contrib.auth.models import *
from django.conf import settings


class seller(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pet_type=models.CharField(max_length=120)
    pet_breed=models.CharField(max_length=120)
    pet_name=models.CharField(max_length=120)
    pet_image=models.ImageField(upload_to='pets_image/')
    pet_age=models.CharField(max_length=20)
    CHOICES=[('MALE', "MALE"), ('FEMALE', "FEMALE")]
    pet_gender=models.CharField(max_length=10, choices=CHOICES)
    pet_price=models.IntegerField()
    pet_description=models.TextField(max_length=200)
    is_sold = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    doctor_reg_no = models.CharField(max_length=120, null=True, blank=True)
    doctor_name = models.CharField(max_length=120, null=True, blank=True)