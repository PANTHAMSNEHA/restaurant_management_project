import os

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#Add to INSTALLED_APPs if not already
INSTALLED_APPS += ['restaurant']