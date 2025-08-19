import requests
from django.shortcuts import render

def home(request):
    response = requests.get('https://your-api-url.com/menu/')  #Replace with actual api
    menu_data = response.json() if response.status_code ==200 else []
    return render(request, 'restaurant_app/home.html',{'menu': menu_data})
    