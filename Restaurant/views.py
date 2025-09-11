from django.shortcuts import render
from .models import Restaurant

def homepage(request):
    restaurant = Restaurant.objects.first()
    return render(request, 'homepage.html',{'restaurant':restaurant})
    

def homepage_view(request):
    return render(request, 'home.html')