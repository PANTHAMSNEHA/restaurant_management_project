from django.urls import path
from .views import homepage_view

urlpattern = [
    path('', homepage_view, name='homepage'),
]