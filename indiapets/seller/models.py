from django.db import models
from django.contrib.auth.models import *
from django.conf import settings


class seller(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Name_choices=[('Dog', "Dog"), ('Cat', "Cat"), ('Buffalo', 'Buffalo'), ('Rabbit', 'Rabbit')]
    Breed_choices=[('German Shepherd', "German shepherd"), ('Labrador', "Labrador"), ('Alaskan', 'Alaskan')]
    pet_name=models.CharField(max_length=120, choices=Name_choices)
    pet_breed=models.CharField(max_length=120, choices=Breed_choices)
    pet_image=models.ImageField(upload_to='pets_image/')
    pet_age=models.CharField(max_length=20)
    CHOICES=[('M', "MALE"), ('F', "FEMALE")]
    pet_gender=models.CharField(max_length=2, choices=CHOICES)
    pet_price=models.IntegerField()
    pet_description=models.TextField(max_length=200)