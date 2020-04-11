
from django.contrib import admin
from django.urls import path
from accounts import views
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from feedback import views as feedback_views
from doctor import views as doctor_views
from django.conf.urls import url,include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('seller/', include('seller.urls')),
    path('',include('pets.urls')),
    path('feedback/', feedback_views.feedback),
    path('Doctor/', doctor_views.index),
]
