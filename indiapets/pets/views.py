from django.shortcuts import render
from . forms import *
from . models import *

# Create your views here.
def all_pets(request):
    pet_s=Animal.objects.all()
    context={'pet_s':pet_s}
    return render(request, 'pets/all_pets.html',context)

def all_breeds(request,pk):
    breed_s=Breed.objects.filter(animal=pk)
    #print(breed_s)
    context={'breed_s':breed_s}
    return render(request,'pets/breeds.html',context)

def breed_info(request,pk):
    breed=Breed.objects.get(breed_id=pk)
    #print(breed.breed_name)
    context={'breed':breed}
    return render(request,'pets/breed_info.html',context)
