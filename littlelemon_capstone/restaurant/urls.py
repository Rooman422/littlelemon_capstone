from django.urls import path, include
from . import views
from .views import BookingListCreateView, BookingDetailView, RegisterView, ApiRootView, BookingFormView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import MenuViewSet, BookingViewSet  # add these if you added viewsets

router = DefaultRouter()
router.register(r'menu', MenuViewSet)
router.register(r'booking', BookingViewSet)

urlpatterns = [
    # Website frontend views
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('book/', views.book, name='book'),
    path('booking-form/', BookingFormView.as_view(), name='booking-form'),

    # API endpoints under /api/
    path('api/', ApiRootView.as_view(), name='api-root'),
    path('api/', include(router.urls)),
    path('api/bookings/', BookingListCreateView.as_view(), name='bookings'),
    path('api/bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
    path('api/registration/', RegisterView.as_view(), name='registration'),

    # Token auth
    path('api/api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
