#views.py

from django.shortcuts import render
from django.http import HttpResponseServerError


def home(request):
    try:
        context = {
        'restaurant_name' : 'Flavours of India'

        }
        return render(request, 'home.html',context)
    except Exception as e:
        return HttpResponseServerError(f"An error occured: {e}")
