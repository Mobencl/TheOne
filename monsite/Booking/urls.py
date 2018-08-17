from django.conf.urls import url
from accounts.views import login_view
from accounts.views import logout_view
from accounts import views
from accounts import forms
from django.conf.urls.static import static
from django.conf import settings
from Booking.views import show_terrains,show_availibility, confirm_booking,show_confirmedbookings,show_bookingsinprogress
from Booking.views import delete_bookinginprogress,delete_confirmedbooking
from Booking.views import show_guests,add_guests
app_name = 'Booking'

urlpatterns = [
    url(r'^player/create/$', show_terrains , name='create'),
    url(r'^player/create/(?P<id>[0-9]+)/availibility/$', show_availibility , name='availibility'),
    url(r'^player/(?P<id>[0-9]+)/confirm/$', confirm_booking , name='confirm'),
    url(r'^player/bookings/confirmed/$', show_confirmedbookings , name='showconfirmedbookings'),
    url(r'^player/bookings/inprogress/$', show_bookingsinprogress , name='showbookingsinprogress'),
    url(r'^profile/bookings/confirmed/(?P<id>[0-9]+)/delete$', delete_confirmedbooking,  name='deleteconfirmedbooking'),
    url(r'^profile/bookings/inprogress/(?P<id>[0-9]+)/delete$', delete_bookinginprogress,  name='deletebookinginprogress'),
    url(r'^player/guests/$', show_guests,  name='showguests'),
    url(r'^player/guests/(?P<id>[0-9]+)/addguests/$', add_guests,  name='addguests'),

]
