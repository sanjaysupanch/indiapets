from django.shortcuts import render
from django.http import FileResponse, Http404

# Create your views here.
from . forms import *
from . models import *


def adoption(request):
    
    adpt=Adoption.objects.all()
    context={'adpt':adpt}
    return render(request, 'adoption/adoption_animal.html',context)

def animal_info(request,pk):
    
    animal=Adoption.objects.filter(pet_id=pk)
    context={'animal':animal}
    # print(animal)
    return render(request,'adoption/animal_info.html',context)

def document(request,pk):
    animal=Adoption.objects.filter(pet_id=pk)
    for a in animal:
        document=a.file
        
    try:
        return FileResponse(open('media/'+str(document), 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()