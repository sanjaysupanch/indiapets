from django.urls import path
from . import views

app_name="pets"

urlpatterns=[

        path('',views.landing,name="landing"),
        path('all_pets/',views.all_pets, name="all_pets"),
        path('all_pets/<pet_type>/',views.all_breed,name="all_breeds"),
        path('pet_info/<id>/<pet_breed>/',views.pet_info,name="pet_info"),
        # path('breed_info/<int:pk>',views.breed_info,name='breed_info'),

]
