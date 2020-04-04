from django.urls import path, include

from accounts import views


urlpatterns= [
    path("profile/", views.address, name="address"),
]