# reservation/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import IntegrityError
from django.contrib import messages
from .models import Train, Person # Assumes models are renamed to Train and Person

# This view now serves as the homepage for the app
def index(request):
    trains = Train.objects.all()
    return render(request, 'viewtrains.html', {"trains": trains})

# --- Authentication ---
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('reservation:train_list')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'login.html')
    # For GET requests, just show the login form
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.create_user(username, email, password)
            auth_login(request, user) # Log in the user after they register
            return redirect('reservation:train_list')
        except IntegrityError:
            messages.error(request, "A user with that username already exists.")
            return render(request, 'register.html')
    # For GET requests, just show the registration form
    return render(request, 'register.html')

def logout_view(request):
    auth_logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('home') # Redirect to the main project homepage

# --- Admin/Superuser Views ---
def is_superuser(user):
    return user.is_superuser

@login_required
@user_passes_test(is_superuser)
def add_train_view(request):
    if request.method == 'POST':
        Train.objects.create(
            source=request.POST.get('source'),
            destination=request.POST.get('destination'),
            time=request.POST.get('time'),
            seats_available=request.POST.get('seats_available'),
            train_name=request.POST.get('train_name'),
            price=request.POST.get('price')
        )
        messages.success(request, "Train added successfully.")
        return redirect('reservation:train_list')
    # For GET requests, show the form to add a train
    return render(request, 'addtrain.html')


def train_detail_view(request, train_id):
    train = get_object_or_404(Train, pk=train_id)
    
    # Initialize an empty list for persons
    persons = []

    # Only fetch the passenger list if the user is a superuser
    if request.user.is_authenticated and request.user.is_superuser:
        persons = train.person_set.all()

    context = {
        'train': train,
        'persons': persons # This will be empty for non-admins
    }
    return render(request, 'viewperson.html', context)

# --- Booking Views ---
@login_required
def booking_form_view(request):
    if request.method == 'POST':
        # This logic should be moved to a Django Form for better validation
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        trains_queryset = Train.objects.filter(source=source, destination=destination)

        if trains_queryset.exists():
            request.session['booking_info'] = {
                'name': request.POST.get('name'),
                'age': request.POST.get('age'),
                'gender': request.POST.get('gender')
            }
            return render(request, 'trainsavailable.html', {'trains': trains_queryset})
        else:
            messages.error(request, "No trains found for the selected route.")
            return redirect('reservation:booking_form')

    # For GET requests, get sources/destinations and show the initial form
    sources = Train.objects.values_list('source', flat=True).distinct()
    destinations = Train.objects.values_list('destination', flat=True).distinct()
    return render(request, 'booking.html', {'sources': sources, 'destinations': destinations})

@login_required
def confirm_booking_view(request, train_id):
    booking_info = request.session.get('booking_info')
    if not booking_info:
        messages.error(request, "Your session has expired. Please search again.")
        return redirect('reservation:booking_form')

    train = get_object_or_404(Train, pk=train_id)
    if train.seats_available <= 0:
        messages.error(request, "Sorry, seats are full on this train.")
        return redirect('reservation:booking_form')
    
    train.seats_available -= 1
    train.save()

    Person.objects.create(
        train=train,
        name=booking_info['name'],
        email=request.user.email,
        age=booking_info['age'],
        gender=booking_info['gender']
    )
    
    del request.session['booking_info']
    
    messages.success(request, f"Booked Successfully! Your ticket for {train.train_name} is confirmed.")
    return redirect('reservation:my_bookings')

@login_required
def my_bookings_view(request):
    booked_persons = Person.objects.filter(email=request.user.email)
    return render(request, 'mybooking.html', {'persons': booked_persons})