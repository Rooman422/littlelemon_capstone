API endpoints for Little Lemon:

POST   /api/registration/      # Register user
POST   /api/token/             # Obtain JWT token
POST   /api/token/refresh/     # Refresh token

GET    /api/bookings/          # List bookings (auth required)
POST   /api/bookings/          # Create booking (auth required)
GET    /api/bookings/<id>/     # Booking detail (auth required)
PUT    /api/bookings/<id>/     # Update booking (auth required)
DELETE /api/bookings/<id>/     # Delete booking (auth required)




http://127.0.0.1:8000/api/booking-form/