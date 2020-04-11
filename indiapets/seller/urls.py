from django.urls import path, include

from seller import views


urlpatterns= [
    path("pets_sell/", views.Pets_details, name="pets_details"),
    path("seller-data/", views.seller_details, name="seller_details"),
]