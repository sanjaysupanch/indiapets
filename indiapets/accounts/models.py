from django.db import models
from django.contrib.auth.models import *
from django.conf import *
# Create your models here.

class CustomUser(AbstractUser):
	first_name = models.CharField(max_length=128, null=True)
	last_name = models.CharField(max_length=128, null=True)
	
	def __str__(self):
		return self.email
