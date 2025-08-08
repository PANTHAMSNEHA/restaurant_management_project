from django.contrib import admin
from django.urls import path
from django.conf import settingd
from django.conf.urls.static import static



utlpatterns = [path('admin/', admin.site.urls),
path('', include())
]