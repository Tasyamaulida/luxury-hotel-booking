from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Room(models.Model):

    ROOM_CATEGORIES = (
        ('STD', 'Standard Room'),
        ('DLX', 'Deluxe Room'),
        ('SUP', 'Superior Room'),
    )

    name = models.CharField(max_length=100)

    category = models.CharField(
        max_length=3,
        choices=ROOM_CATEGORIES
    )

    total_rooms = models.IntegerField(default=10)

    available_rooms = models.IntegerField(
        default=10
    )

    capacity = models.IntegerField()

    price = models.IntegerField()

    image = models.ImageField(
        upload_to='rooms/'
    )

    description = models.TextField()

    def save(self, *args, **kwargs):

        if not self.available_rooms:
            self.available_rooms = self.total_rooms

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Booking(models.Model):

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Checked In', 'Checked In'),
        ('Cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE
    )

    check_in = models.DateField()

    check_out = models.DateField()

    guests = models.IntegerField(default=1)

    total_price = models.IntegerField(default=0)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):

        if isinstance(self.check_in, str):
            self.check_in = datetime.strptime(
                self.check_in,
                "%Y-%m-%d"
            ).date()

        if isinstance(self.check_out, str):
            self.check_out = datetime.strptime(
                self.check_out,
                "%Y-%m-%d"
            ).date()

        nights = (
            self.check_out - self.check_in
        ).days

        if nights < 1:
            nights = 1

        self.total_price = (
            self.room.price * nights
        )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.room.name}"


class RoomBlock(models.Model):

    STATUS_CHOICES = (
        ('maintenance', 'Maintenance'),
        ('renovation', 'Renovation'),
        ('closed', 'Closed'),
    )

    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    note = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.room.name} - {self.date}"