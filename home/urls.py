from django.urls import path
from .views import *

urlpatterns = [
    path(' ',TemplateView.as_view(template_name='index.html'),name='home'),
    
]