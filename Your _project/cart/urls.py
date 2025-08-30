from django.urls import path
from .views import homepage
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',homepage, name='homepage'),
    path('admin/',admin.site.urls),
    path('', include('cart.urls')),   #Include Cart app
]