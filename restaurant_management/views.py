from django.shortcuts import render
from django.http import HttpResponseServerError

def reservations(request):
    try:
        content = {
            'message': 'Reservations page coming soon!'
        }
        return render(request, 'reservations.html', context)
    except Exception as e:
        return HttpResponseServerError(f"An error occured: {e}")