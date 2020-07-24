from django.shortcuts import render
from . forms import *
from . models import *
from seller.models import *
# Create your views here.
def all_pets(request):
    pet_s=Animal.objects.all()
    # for i in pet_s:
        # print(i.animal_name)
    context={'pet_s':pet_s}
    return render(request, 'pets/all_pets.html',context)

# def all_breeds(request,pk):
#     breed_s=Breed.objects.filter(animal=pk)
#     #print(breed_s)
#     context={'breed_s':breed_s}
#     return render(request,'pets/breeds.html',context)

# def breed_info(request,pk):
#     breed=Breed.objects.get(breed_id=pk)
#     #print(breed.breed_name)
#     context={'breed':breed}
#     return render(request,'pets/breed_info.html',context)




#landing_page<====

def landing(request):
    return render(request, 'pets/landing_page.html', {})

def all_breed(request, **kwargs):
    pet_type = kwargs['pet_type']
    breed_data = seller.objects.filter(pet_type=pet_type)
    return render(request, 'pets/breed.html', {'breed':breed_data})

def pet_info(request, **kwargs):
    ids = int(kwargs['id'])
    pet_breed=kwargs['pet_breed']
    info = seller.objects.filter(id=ids)
    breed = Breed.objects.filter(breed_name=pet_breed)
    info_breed= zip(info, breed)

    return render(request, 'pets/info.html', {'info':info, 'breed': info_breed})