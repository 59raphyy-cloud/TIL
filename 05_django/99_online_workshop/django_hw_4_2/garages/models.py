from django.db import models

# Create your models here.
class Garage(models.Model):
    location = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField(default=0)
    is_parking_available = models.BooleanField(default=True)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    
    def __str__(self):
        return f"{self.location} ({self.capacity} slots)"