from django.test import TestCase
from django.contrib.auth.models import User
from core.models import TravelOption, Booking
from django.utils import timezone
from datetime import timedelta

class TravelModelTests(TestCase):
    def setUp(self):
        self.travel = TravelOption.objects.create(
            type='Flight',
            source='Delhi',
            destination='Mumbai',
            date_time=timezone.now() + timedelta(days=2),
            price=3000,
            available_seats=100
        )

    def test_travel_created(self):
        self.assertEqual(self.travel.source, 'Delhi')
        self.assertTrue(self.travel.available_seats > 0)

class BookingModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='mahak', password='testpass')
        self.travel = TravelOption.objects.create(
            type='Bus',
            source='A',
            destination='B',
            date_time=timezone.now() + timedelta(days=1),
            price=500,
            available_seats=40
        )
        self.booking = Booking.objects.create(
            user=self.user,
            travel=self.travel,
            seats=2,
            total_price=1000,
            status='Confirmed'
        )

    def test_booking_total_price(self):
        self.assertEqual(self.booking.total_price, 1000)

    def test_booking_status(self):
        self.assertEqual(self.booking.status, 'Confirmed')
