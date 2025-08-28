from django.db import models

class RestaurantLocation(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    

    description = models.TextField()

    #Opening hours stored as a JSON field(dictionary format)
    opening_hours = models.JSONField(default=dict)

    opening_hours={
        "Monday": "9.00AM - 9:00PM",
        "Tuesday": "9.00 AM - 9:00 PM",
        "Wednesday":"Closed",
        "Thursday":"9.00 AM - 9.00PM",
        "Friday":"9.00 AM - 10.00PM",
        "Saturday": "10:00 AM - 10:00PM"
        "Sunday":"10:00 AM - 8:00 PM"
    }

    def __str__(self):
        return f"{self.address},{self.city}, {self.state} {self.zip_code}"