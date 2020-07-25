from django import forms
import datetime
from . models import *

class Adoptionform(forms.ModelForm):
    class Meta:
        model=Adoption
        fields='__all__'