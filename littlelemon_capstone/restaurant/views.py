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
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer



def index(request):
    return render(request, 'index.html')

from rest_framework.permissions import AllowAny

class BookingListCreateView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [AllowAny]  

    def get_queryset(self):
        queryset = Booking.objects.all()
        booking_date = self.request.query_params.get('date')
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


def about(request):
    return render(request, 'about.html')



def menu(request):
    return render(request, 'menu.html')


def book_view(request):
    return render(request, 'book.html')



def book(request):
    return render(request, 'book.html')





class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
