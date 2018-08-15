from django.conf.urls import url
from accounts.views import login_view
from accounts.views import logout_view
from accounts import views
from accounts import forms
from django.conf.urls.static import static
from django.conf import settings
from Booking.views import show_terrains,show_availibility, confirm_booking



app_name = 'Booking'

urlpatterns = [
    url(r'^player/create/$', show_terrains , name='create'),
    url(r'^player/create/(?P<id>[0-9]+)/availibility/$', show_availibility , name='availibility'),
    url(r'^player/(?P<id>[0-9]+)/confirm/$', confirm_booking , name='confirm'),
    #url(r'^player/bookings/confirmed/$', show_confirmedbookings , name='showconfirmedbookings'),
    #url(r'^player/bookings/inprogress/$', show_bookingsinprogress , name='showbookingsinprogress'),
]
