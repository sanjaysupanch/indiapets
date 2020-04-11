from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm, AllauthSignupForm
from .models import *

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    form1=AllauthSignupForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name']

# class AllauthSignupForm()
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Address)