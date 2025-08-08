from django.contrib import admin
from django.urls import path,
from django.conf import settinga
from django.conf.urls.static import static

urlpatterns = [
    pat('admin/',admin.site.urls),
    path('', include('homepage_app.urls')),
]

if settings.DEBUG:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])