from django.urls import path
from.views import order_confirmation

urlpatterns = [

    path('confirm/', order_confirmation, name="oredr_confirmation"),
]