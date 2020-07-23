from django.urls import path
from . import views

app_name="pets"

urlpatterns=[

        path('',views.landing,name="landing"),
        # path('',views.all_pets,name="all_pets"),
        path('all_breed/<int:pk>',views.all_breeds,name="all-breed"),
        path('breed_info/<int:pk>',views.breed_info,name='breed_info'),

]
