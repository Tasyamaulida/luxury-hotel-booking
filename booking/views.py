from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Room, Booking


# ==========================================
# HOME
# ==========================================

def home(request):
    rooms = Room.objects.all()[:3]

    return render(
        request,
        'home.html',
        {
            'rooms': rooms
        }
    )


# ==========================================
# ROOM LIST
# ==========================================

def room_list(request):

    rooms = Room.objects.all()

    return render(
        request,
        'kamar.html',
        {
            'rooms': rooms
        }
    )


# ==========================================
# FACILITIES
# ==========================================

def facility_view(request):
    return render(request, 'fasilitas.html')


# ==========================================
# ABOUT
# ==========================================

def about_view(request):
    return render(request, 'tentang_kami.html')


# ==========================================
# REGISTER
# ==========================================

def register_view(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:

            messages.error(
                request,
                "Konfirmasi password tidak sesuai!"
            )

            return render(
                request,
                'register.html'
            )

        if User.objects.filter(
            username=email
        ).exists():

            messages.error(
                request,
                "Akun sudah terdaftar sebelumnya! Silakan login."
            )

            return render(
                request,
                'register.html'
            )

        try:

            user = User.objects.create_user(
                username=email,
                email=email,
                password=password
            )

            user.save()

            messages.success(
                request,
                "Pendaftaran berhasil! Silakan masuk."
            )

            return redirect('login')

        except Exception as e:

            messages.error(
                request,
                f"Error: {e}"
            )

            return render(
                request,
                'register.html'
            )

    return render(
        request,
        'register.html'
    )


# ==========================================
# LOGIN
# ==========================================

def login_view(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(
            username=email,
            password=password
        )

        if user is not None:

            login(request, user)

            messages.success(
                request,
                "Login Berhasil!"
            )

            return redirect('room_list')

        else:

            messages.error(
                request,
                "Email atau password salah!"
            )

            return render(
                request,
                'login.html'
            )

    return render(
        request,
        'login.html'
    )


# ==========================================
# LOGOUT
# ==========================================

def logout_view(request):

    logout(request)

    messages.success(
        request,
        "Logout Berhasil!"
    )

    return redirect('home')


# ==========================================
# BOOKING ROOM
# ==========================================

@login_required(login_url='login')
def booking_room(request, room_id):

    room = get_object_or_404(
        Room,
        id=room_id
    )

    if request.method == 'POST':

        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        guests = request.POST.get('guests')

        Booking.objects.create(
            user=request.user,
            room=room,
            check_in=check_in,
            check_out=check_out,
            guests=guests,
            status='Pending'
        )

        messages.success(
            request,
            "Booking berhasil dibuat!"
        )

        return redirect('my_bookings')

    return render(
        request,
        'booking_form.html',
        {
            'room': room
        }
    )


# ==========================================
# MY BOOKINGS
# ==========================================

@login_required(login_url='login')
def my_bookings(request):

    bookings = Booking.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'my_bookings.html',
        {
            'bookings': bookings
        }
    )


# ==========================================
# AVAILABILITY
# ==========================================

def availability_view(request):

    rooms = Room.objects.all()

    return render(
        request,
        'admin/availability.html',
        {
            'rooms': rooms
        }
    )