#views.py

from django.shortcuts import render


def home(request):
    context = {
        'restaurant_name' : 'Flavours of India'

    }
    return render(request, 'home.html',context)