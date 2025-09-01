from django.db import models

class RestaurantInfo(models.Model):
    phone = models.CharField(max_length=20)


    def __str__(self):
        return self.phone