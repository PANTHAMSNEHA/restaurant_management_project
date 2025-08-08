from django.urls import path
from . import views

utlpatterns = [path('',views.home_view, name='home'),
]