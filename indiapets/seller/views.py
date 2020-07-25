from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.serializers import *
from rest_framework import viewsets, permissions, status, generics
from rest_framework.generics import * 
from .serializers import SellerSerializer

from django.shortcuts import *
from .forms import *
from .models import *
from seller.models import *
from django.urls import reverse_lazy
from accounts.models import *




@login_required
def Pets_details(request):
    print(request.user, "2222")
    if request.method =="POST":
        form=sellerForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('/seller/seller-data/')
        else:
            return HttpResponse("Form is invalid")
    else:
        form=sellerForm()
        return render(request, 'seller/pets_sell.html', {'form':form})

@login_required
def seller_details(request):
    user_instance=CustomUser.objects.get(email=request.user)
    seller_data=seller.objects.filter(user=user_instance)
    
    return render(request, 'seller/seller_details.html', {'seller_data':seller_data})


class SellerView(generics.ListCreateAPIView):
    queryset=seller.objects.all()
    serializer_class=SellerSerializer

class SellerUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset=seller.objects.all()
    serializer_class=SellerSerializer
    lookup_field='id'
    