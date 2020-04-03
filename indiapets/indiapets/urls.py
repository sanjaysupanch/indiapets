
from django.contrib import admin
from django.urls import path, include
# from accounts import views
# from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    # path('', views.index),
    path('doctor/',include('doctor.urls')),
]
