# reservation/urls.py

from django.urls import path
from . import views

# This is a best practice for making URL names unique across your project
app_name = 'reservation'

urlpatterns = [
    # The homepage for the app is the train list
    path('', views.index, name="train_list"),
    
    # Authentication URLs
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('logout/', views.logout_view, name="logout"),
    
    # Admin-related URLs for adding and viewing train details
    path('trains/add/', views.add_train_view, name="add_train"),
    path('trains/<int:train_id>/', views.train_detail_view, name="train_detail"),
    
    # Booking process URLs
    path('booking/', views.booking_form_view, name="booking_form"),
    path('booking/confirm/<int:train_id>/', views.confirm_booking_view, name="confirm_booking"),
    path('my-bookings/', views.my_bookings_view, name="my_bookings"),
]