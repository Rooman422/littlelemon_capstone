Little Lemon Capstone Project - API Endpoints for Peer Review

This project implements a backend API for the Little Lemon restaurant using Django REST Framework, connected to a MySQL database, with user authentication and unit tests.

API endpoints to test:

1. Booking API:
   - List all bookings: GET /api/bookings/
   - Create a booking: POST /api/bookings/
   - Retrieve a booking: GET /api/bookings/<id>/
   - Update a booking: PUT /api/bookings/<id>/
   - Delete a booking: DELETE /api/bookings/<id>/

2. Menu API:
   - List all menu items: GET /api/menu/
   - Create a menu item: POST /api/menu/
   - Retrieve a menu item: GET /api/menu/<id>/
   - Update a menu item: PUT /api/menu/<id>/
   - Delete a menu item: DELETE /api/menu/<id>/

3. User Registration and Authentication:
   - Register user: POST /api/registration/
   - Obtain auth token: POST /api/api-token-auth/

Testing:

- The project contains unit tests located in:
  - restaurant/app_tests/test_models.py
  - restaurant/app_tests/test_views.py

- You can test the API using the Browsable API provided by Django REST Framework or with the Insomnia REST Client.

Please clone this repository, set up the project according to the instructions in the code, and use the above API endpoints for testing.

Thank you!
