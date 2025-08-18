from django.contrib import admin
from .models import Menu, Order

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name','price','category')  #Customize  based on your model fields

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name','menu_item','quantity','status')  # Adjust as needed