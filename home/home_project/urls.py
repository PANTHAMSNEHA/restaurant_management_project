from django.contrib import admin
from django.urls import path,
from django.conf import settinga
from django.conf.urls.static import static

urlpatterns = [
    pat('admin/',admin.site.urls),
    path('', include('homepage_app.urls'))
    
]