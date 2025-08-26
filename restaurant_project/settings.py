import os

MEDIA_URL = '/media'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#Also add this to your main urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(sttings.MEDIA_URL, document_root=settings.MEDIA_ROOT)