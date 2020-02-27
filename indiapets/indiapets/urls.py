
from django.contrib import admin
from django.urls import path
from accounts import views
from django.conf.urls import url,include 

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('home/', views.home),
    path('', views.index),
]
