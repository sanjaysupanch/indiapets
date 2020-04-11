from django.db import models
from django.contrib.auth.models import *
from django.conf import *
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
	first_name = models.CharField(max_length=128, null=True)
	last_name = models.CharField(max_length=128, null=True)
	
	def __str__(self):
		return self.email

class Address(models.Model):
	user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	state=models.CharField(max_length=50, blank=True)
	district=models.CharField(max_length=40)
	pin=models.IntegerField()
	street_name=models.CharField(max_length=120)
	house_number=models.CharField(max_length=10)
	contact_no=models.BigIntegerField(unique=True)

