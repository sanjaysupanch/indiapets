from django.shortcuts import render
from . forms import *
from . models import *
from seller.models import *


# @login_required
def all_pets(request):
    pet_s=Animal.objects.all()
    context={'pet_s':pet_s}
    return render(request, 'pets/all_pets.html',context)



#landing_page<====

def landing(request):
    return render(request, 'pets/landing_page.html', {})

# @login_required
def all_breed(request, **kwargs):
    pet_type = kwargs['pet_type']
    breed_data = seller.objects.filter(pet_type=pet_type)
    return render(request, 'pets/breed.html', {'breed':breed_data})
# @login_required
def pet_info(request, **kwargs):
    ids = int(kwargs['id'])
    pet_breed=kwargs['pet_breed']
    info = seller.objects.filter(id=ids)
    breed = Breed.objects.filter(breed_name=pet_breed)
    info_breed= zip(info, breed)

    return render(request, 'pets/info.html', {'info':info, 'breed': info_breed})