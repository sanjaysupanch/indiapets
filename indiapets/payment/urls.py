from django.conf.urls import url
from django.urls import path
from . import views

# app_name = "payment"

urlpatterns = [
    
    path('process/<id>/<pet_price>/<pet_name>/', views.process_payment, name='process_payment'),
    path('done/', views.payment_done, name='payment_done'),
    path('cancelled/', views.payment_canceled, name='payment_cancelled'),
]