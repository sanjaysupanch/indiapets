
from django.contrib import admin
from django.urls import path
from accounts import views
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('', views.index),
    path('pets/',include('pets.urls')),

]
