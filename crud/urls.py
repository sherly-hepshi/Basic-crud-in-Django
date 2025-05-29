from django.urls import path
from . import views

urlpatterns = [
    path('', views.read_bookings, name='read_bookings'),
    path('create/', views.create_booking, name='create_booking'),
    path('update/<str:booking_id>/', views.update_booking, name='update_booking'),
    path('delete/<str:booking_id>/', views.delete_booking, name='delete_booking'),
]
