from django import forms
import datetime
from . models import *

class Petform(forms.ModelForm):
    class Meta:
        model=Animal
        fields='__all__'


class Breedform(forms.ModelForm):
    class Meta:
        model=Breed
        fields='__all__'
