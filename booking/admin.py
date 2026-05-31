from django.contrib import admin
from django.db.models import Sum
from django.contrib.auth.models import User
from django.urls import path
from django.template.response import TemplateResponse
from django.shortcuts import redirect
from datetime import date

from .models import Room, Booking


# ======================================================
# CUSTOM ADMIN SITE
# ======================================================

class HotelAdminSite(admin.AdminSite):

    site_header = "Luxury Hotel Admin"
    site_title = "Luxury Hotel"
    index_title = "Dashboard"

    def index(self, request, extra_context=None):

        total_rooms = Room.objects.aggregate(
            total=Sum('total_rooms')
        )['total'] or 0

        dashboard_rooms = []

        for room in Room.objects.all():

            confirmed = Booking.objects.filter(
                room=room,
                status='Confirmed'
            ).count()

            available = room.total_rooms - confirmed

            if available < 0:
                available = 0

            if room.total_rooms > 0:
                percent = int(
                    (available / room.total_rooms) * 100
                )
            else:
                percent = 0

            dashboard_rooms.append({
                'name': room.name,
                'image': room.image,
                'percent': percent,
            })

        confirmed_bookings = Booking.objects.filter(
            status='Confirmed'
        ).count()

        available_rooms = total_rooms - confirmed_bookings

        if available_rooms < 0:
            available_rooms = 0

        today_checkins = Booking.objects.filter(
            check_in=date.today(),
            status='Confirmed'
        ).count()

        context = {
            'total_bookings': Booking.objects.count(),
            'total_customers': User.objects.count(),
            'total_rooms': total_rooms,
            'available_rooms': available_rooms,
            'today_checkins': today_checkins,
            'recent_bookings': Booking.objects.all().order_by('-id')[:5],
            'dashboard_rooms': dashboard_rooms,
        }

        extra_context = extra_context or {}
        extra_context.update(context)

        return super().index(request, extra_context)

    def update_booking_status(
        self,
        request,
        booking_id,
        status
    ):

        booking = Booking.objects.get(
            id=booking_id
        )

        booking.status = status
        booking.save()

        return redirect(
            '/admin/booking/booking/'
        )

    def get_urls(self):

        urls = super().get_urls()

        custom_urls = [

            path(
                'customers/',
                self.admin_view(
                    self.customers_view
                ),
                name='customers',
            ),

            path(
                'booking-status/<int:booking_id>/<str:status>/',
                self.admin_view(
                    self.update_booking_status
                ),
                name='update_booking_status',
            ),

        ]

        return custom_urls + urls

    def customers_view(self, request):

        users = User.objects.all().order_by(
            '-date_joined'
        )

        context = dict(
            self.each_context(request),
            customers=users,
            total_customers=users.count(),
        )

        return TemplateResponse(
            request,
            "admin/customers.html",
            context
        )


# ======================================================
# REGISTER CUSTOM ADMIN
# ======================================================

admin_site = HotelAdminSite(
    name='hotel_admin'
)


# ======================================================
# ROOM ADMIN
# ======================================================

@admin.register(Room, site=admin_site)
class RoomAdmin(admin.ModelAdmin):

    change_list_template = "admin/room_list.html"
    change_form_template = "admin/room_form.html"

    fields = (
        'name',
        'category',
        'total_rooms',
        'available_rooms',
        'capacity',
        'price',
        'image',
        'description',
    )

    list_display = (
        'name',
        'category',
        'price',
        'total_rooms',
        'available_rooms',
    )

    search_fields = (
        'name',
        'category',
    )

    list_filter = (
        'category',
    )


# ======================================================
# BOOKING ADMIN
# ======================================================

@admin.register(Booking, site=admin_site)
class BookingAdmin(admin.ModelAdmin):

    change_list_template = "admin/booking_list.html"

    list_display = (
        'user',
        'room',
        'check_in',
        'check_out',
        'status',
        'total_price',
    )

    search_fields = (
        'user__username',
        'room__name',
    )

    list_filter = (
        'status',
    )