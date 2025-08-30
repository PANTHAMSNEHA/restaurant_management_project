from django.db import models

class RestaurantInfo(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/')     #Save in media/logos/