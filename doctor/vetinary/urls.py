from django.urls import include, path
from . import views
from .views import *


urlpatterns= [
    path('', views.pet_data, name='pet-data'),
    path('<id>/', views.pet_update, name='pet-update'),
    
]