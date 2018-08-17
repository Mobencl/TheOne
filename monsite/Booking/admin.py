from django.contrib import admin
from Booking.models import Booking_inprogress, Guest

admin.site.register(Booking_inprogress)
admin.site.register(Guest)
