from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    context= { "a": "This is a context "}
    return render(request, 'accounts/home.html', context=context)


def index(request):
    context= { "a": "This is a context "}
    return render(request, 'accounts/san.html', context=context)
