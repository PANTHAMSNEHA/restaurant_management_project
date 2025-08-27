from django.conf import path
from . import views

urlpatterns = [
    path('',views.homepage, name='homepage'),
]