from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveIntegerField()
    booking_date = models.DateField()
    booking_time = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.booking_date} at {self.booking_time}"
