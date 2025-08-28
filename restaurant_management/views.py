import requests
from django.shortcuts import render
from .models import MenuItem


def home(request):
    response = requests.get('https://your-api-url.com/menu/')  #Replace with actual api
    menu_data = response.json() if response.status_code ==200 else []
    return render(request, 'restaurant_app/home.html',{'menu': menu_data})
    

def menu_view(request):
    items = MenuItem.objects.all()
    return render(request, 'menu.html',{'items':items})