from rest_framework import generics, permissions
from .models import Booking
from .serializers import BookingSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

class BookingListCreateView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Booking.objects.all()
        booking_date = self.request.query_params.get('booking_date')
        if booking_date:
            queryset = queryset.filter(booking_date=booking_date)
        return queryset

class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class BookingFormView(TemplateView):
    template_name = "booking.html"


class ApiRootView(APIView):
    def get(self, request):
        return Response({
            'bookings': '/api/bookings/',
            'registration': '/api/registration/',
            'token': '/api/token/',
        })