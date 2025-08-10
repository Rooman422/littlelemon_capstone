from django.test import TestCase
from restaurant.models import Booking

class BookingModelTest(TestCase):
    def test_booking_creation(self):
        booking = Booking.objects.create(
            name='John Doe',
            booking_date='2025-08-10',
            reservation_slot='12:00',
            no_of_guests=2
        )
        self.assertEqual(booking.name, 'John Doe')
        self.assertEqual(booking.booking_date, '2025-08-10')
        self.assertEqual(booking.reservation_slot, '12:00')
        self.assertEqual(booking.no_of_guests, 2)
