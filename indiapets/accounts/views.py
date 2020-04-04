from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import *
from .forms import *
from .models import *
from accounts.models import CustomUser
# from django.urls import reverse_lazy
from django.http import HttpResponse

def index(request):
    context= { "a": "This is a context "}
    return render(request, 'accounts/index.html', context=context)

@login_required
def address(request):
    user_instance=CustomUser.objects.get(email=request.user)
    if(Address.objects.filter(user=user_instance).exists()):
        profile_data=Address.objects.get(user=user_instance)
        if(profile_data.pin != None): 
            return redirect('/')
    
    elif request.method == "POST":
        form=AddressForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('/')
    else:
        form=AddressForm()
        return render(request, 'accounts/profile.html', {'form':form})



