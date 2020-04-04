from django.db import models

# Create your models here.
class Animal(models.Model):
    animal_id=models.AutoField(primary_key=True)
    animal_name=models.CharField(max_length=50,null=False)
    def __str__(self):
        return str(self.animal_name)

class Breed(models.Model):
    breed_id=models.AutoField(primary_key=True)
    breed_name=models.CharField(max_length=50,null=False)
    lifespan=models.IntegerField()
    gestation_period=models.IntegerField()
    average_height=models.FloatField()
    daily_sleep=models.IntegerField()
    diet_chart=models.CharField(max_length=1000)
    animal=models.ForeignKey(Animal,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.breed_name)
