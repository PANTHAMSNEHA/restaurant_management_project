from django.contrib import admin
from .models import MenuItem
from you_app.models import RestaurantInfo
RestaurantInfo.objects.create(phone="+91-9234567789")

admin.site.register(MenuItem)