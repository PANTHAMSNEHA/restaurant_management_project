#views.py

from django.shortcuts import render
from django.conf import settings

def home(request):
    context = {
        'phone_number': settings.RESTAURANT_PHONE_NUMBER

    }
    return render(request, 'home/home.html',context)