frrom your_app.models import RestaurantInfo

def homepage(request):
    info = RestauarantInfo.objects.first()

    content = {
        'phone': info.phone if info else "Phone number not available"

    }
    return render(request, 'home/homepage.html',content)