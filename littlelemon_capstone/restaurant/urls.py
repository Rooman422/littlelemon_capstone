from django.urls import path
from .views import BookingListCreateView, BookingDetailView, RegisterView, ApiRootView
from .views import BookingFormView


urlpatterns = [
    path('', ApiRootView.as_view(), name='api-root'),
    path('bookings/', BookingListCreateView.as_view(), name='bookings'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
    path('registration/', RegisterView.as_view(), name='registration'),


    path('booking-form/', BookingFormView.as_view(), name='booking-form'), 
]
