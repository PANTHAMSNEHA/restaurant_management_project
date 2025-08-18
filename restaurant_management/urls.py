from django.urls import path
from .views_api import MenuAPIView
urlpatterns = [
    path('api/menu/', MenuAPIView.as_view(), name='menu-api'),
]