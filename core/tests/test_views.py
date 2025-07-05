from django.test import TestCase, Client
from django.contrib.auth.models import User
from core.models import TravelOption
from django.utils import timezone
from datetime import timedelta

class TravelViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='mahak', password='testpass')
        self.travel = TravelOption.objects.create(
            type='Train',
            source='Jaipur',
            destination='Agra',
            date_time=timezone.now() + timedelta(days=1),
            price=400,
            available_seats=10
        )

    def test_travel_list_view(self):
        response = self.client.get('/travels/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Jaipur')

    def test_booking_requires_login(self):
        response = self.client.get(f'/book/{self.travel.pk}/')
        self.assertEqual(response.status_code, 302)  # redirects to login

    def test_booking_confirmed(self):
        self.client.login(username='mahak', password='testpass')
        response = self.client.post(f'/book/{self.travel.pk}/', {'seats': 1})
        self.assertEqual(response.status_code, 302)  # redirect after booking
