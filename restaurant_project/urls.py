from django.conf import path
from . import views
from django.urls import path
from .views import order_confirmation


urlpatterns = [
    path('',views.homepage, name='homepage'),
    path('admin/',admin.site.urls),
    path('orders/', include('orders.urls')), #now accessible at /orders/confirm/
]