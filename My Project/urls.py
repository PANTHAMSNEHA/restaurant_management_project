from django.urls import path
from .views import login_view

urlpatterns = [
    path('',views.home, name="home"),
    path('contact/',views,contact, name='contact'),
    path('feedback/',views.feedback, name='feedback'),
    path('login/',login_view, name='login')
]