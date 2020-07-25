from django.db import models

# Create your models here.
class Adoption(models.Model):
    
    pet_id=models.AutoField(primary_key=True)
    pet_name=models.CharField(max_length=120)
    pet_breed=models.CharField(max_length=120)
    pet_image=models.ImageField(upload_to='adopt_image/')
    pet_age=models.CharField(max_length=20)
    CHOICES=[('MALE', "MALE"), ('FEMALE', "FEMALE")]
    pet_gender=models.CharField(max_length=10, choices=CHOICES)
    pet_description=models.TextField(max_length=200)
    lifespan=models.IntegerField()
    gestation_period=models.IntegerField()
    average_height=models.FloatField()
    daily_sleep=models.IntegerField()
    Food=models.TextField(max_length=1000)
    file=models.FileField(upload_to='adopt_files/')