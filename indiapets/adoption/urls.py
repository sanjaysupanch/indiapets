from django.urls import path
from . import views

app_name="adoption"

urlpatterns=[

        path('adoption/',views.adoption,name="adoption"),
        path('animal_info/<int:pk>',views.animal_info,name='animal_info'),
        path('document/<int:pk>',views.document,name="document")

]
