
from django.contrib import admin
from django.urls import path
from accounts import views
<<<<<<< HEAD
from django.conf.urls import url,include 
from django.conf import settings
from django.conf.urls.static import static
=======
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from feedback import views as feedback_views
>>>>>>> fa1c1fd4ab368acf30f9c40b864afbd0f5480899

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('seller/', include('seller.urls')),
    path('', views.index),
<<<<<<< HEAD

] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    path('pets/',include('pets.urls')),
    path('feedback/', feedback_views.feedback),
]
>>>>>>> fa1c1fd4ab368acf30f9c40b864afbd0f5480899
