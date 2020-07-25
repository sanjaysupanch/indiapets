from django.urls import include, path
from seller import views
from seller.views import *


urlpatterns= [
    path("seller/", SellerView.as_view()),
    path("seller/<id>/", SellerUpdateView.as_view()),
    
]