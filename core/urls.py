from django.urls import path
from booking import views
from booking.admin import admin_site

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # ==========================
    # ADMIN PANEL
    # ==========================
    path('admin/', admin_site.urls),

    # ==========================
    # WEBSITE
    # ==========================
    path('', views.home, name='home'),
    path('kamar/', views.room_list, name='room_list'),
    path('fasilitas/', views.facility_view, name='facilities'),
    path('tentang-kami/', views.about_view, name='about'),

    # ==========================
    # AUTH
    # ==========================
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    # ==========================
    # BOOKING USER
    # ==========================
    path(
        'booking/<int:room_id>/',
        views.booking_room,
        name='booking_room'
    ),

    path(
        'my-bookings/',
        views.my_bookings,
        name='my_bookings'
    ),

] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)