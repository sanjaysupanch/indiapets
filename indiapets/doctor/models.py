from django.db import models

# Create your models here.
class Specialization(models.Model):
    specialization_id = models.IntegerField(primary_key=True, max_length=20)
    specialization_name = models.CharField(max_length=100)

    def __str__(self):
        return self.specialization_name
