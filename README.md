Little Lemon Capstone Project
This backend API project for the Little Lemon restaurant is built with Django and Django REST Framework.

Project Overview
Provides a RESTful API to manage restaurant menu items and table bookings.

Supports user registration and authentication.

Connects to a MySQL database for data storage.

Includes unit tests for models and views.

Designed to be tested easily with tools like Insomnia or Postman.

Getting Started
Clone the repository:
git clone https://github.com/Rooman422/littlelemon_capstone.git
cd littlelemon_capstone
Create and activate a virtual environment:

python -m venv .venv
.\.venv\Scripts\activate

On Linux/macOS:
python -m venv .venv
source .venv/bin/activate

Install dependencies:
pip install -r requirements.txt
Set up your MySQL database and update settings.py with your database credentials.

Run database migrations:

python manage.py migrate
Start the development server:

python manage.py runserver
API Endpoints
/api/bookings/ — List all bookings (GET) or create a new booking (POST).

/api/bookings/<id>/ — Retrieve, update, or delete a specific booking.

/api/menu/ — Retrieve menu items.

/api/registration/ — User registration.

/api/api-token-auth/ — Obtain authentication token (login).

Testing
Run unit tests with:

python manage.py test

Notes:

Ensure the environment variable DJANGO_SETTINGS_MODULE=littlelemon.settings is set if required.

This project uses Django REST Framework and Djoser for authentication.

