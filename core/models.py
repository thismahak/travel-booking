from django.db import models
from django.contrib.auth.models import User

class TravelOption(models.Model):
    TRAVEL_TYPES = (
        ('Flight', 'Flight'),
        ('Train', 'Train'),
        ('Bus', 'Bus'),
    )

    travel_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=10, choices=TRAVEL_TYPES)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.type}: {self.source} → {self.destination} ({self.date_time.date()})"

class Booking(models.Model):
    STATUS_CHOICES = (
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    )

    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    travel = models.ForeignKey(TravelOption, on_delete=models.CASCADE)
    seats = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booked_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Confirmed')

    def __str__(self):
        return f"{self.user.username} - {self.travel} ({self.seats} seat(s))"
