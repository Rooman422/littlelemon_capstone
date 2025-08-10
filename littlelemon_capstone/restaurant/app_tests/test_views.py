from rest_framework.test import APITestCase
from django.urls import reverse
from restaurant.models import Booking

class BookingViewTest(APITestCase):
    def test_create_booking(self):
        url = reverse('bookings')
        data = {
            "name": "Jane Smith",
            "booking_date": "2025-08-15",
            "reservation_slot": "18:00",
            "no_of_guests": 4
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Booking.objects.count(), 1)
        booking = Booking.objects.first()
        self.assertEqual(booking.name, "Jane Smith")
        self.assertEqual(booking.no_of_guests, 4)
