from django.contrib.auth import authenticate
from django.contrib.auth import  login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse
from accounts.forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from accounts.models import Terrain
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from accounts.forms import AddTerrainView,AvailibilityForm
from accounts.models import ProfileUser, Aivailibility
from Booking.forms import BookingProgress
from Booking.models import Booking_inprogress
import uuid
from django.contrib.auth.models import User

def show_terrains(request):
        user=request.user
        terrains_list=Terrain.objects.all()
        return render(request,'player/showterrain.html',{'Terrain': terrains_list})
#def extraction():
#

def show_availibility(request,id):
    terrain = Terrain.objects.get(id=id)
    availibility_list = Aivailibility.objects.filter(availibility=terrain)
    form=BookingProgress(request.POST or None)
    if request.method =='POST':
        if form.is_valid():
            bookingFromTill=form.save(commit=False)
            bookingFromTill.terrain = terrain
            bookingFromTill.user=request.user
            bookingFromTill.booking_id = uuid.uuid4()
            bookingFromTill.status=0
            bookingFromTill.save()
            bookingid = bookingFromTill.booking_id
            booking = Booking_inprogress.objects.get(booking_id = bookingid)

            return render(request,'player/bookinginprogress.html',{'Booking_inprogress':booking ,'Terrain':terrain })
    return render(request,'player/showavailibility.html',{'Aivailibility': availibility_list, 'form': form })

def confirm_booking(request,id):
    user=request.user
    booking_inprogress = Booking_inprogress.objects.get(id=id)
    booking_inprogress.status = 1
    booking_inprogress.save()
    new_availibility = Aivailibility()
    new_availibility.notAvailableFrom= booking_inprogress.bookingFrom
    new_availibility.notAvailableTill= booking_inprogress.bookingUntil
    new_availibility.availibility= booking_inprogress.terrain
    new_availibility.save()
    #Confirmed booking the default 0 is for a booking in progress
    return render(request,'player/show_booking.html',{'Booking_inprogress': booking_inprogress})

def show_confirmedbookings(request):
    user=request.user
    confirmedbooking_list = Booking_inprogress.objects.filter(user=user).filter(status=1)
    return render(request,'player/confirmed_bookings.html',{'Booking_inprogress': confirmedbooking_list})

def show_bookingsinprogress(request):
    user=request.user
    bookinginprogress_list = Booking_inprogress.objects.filter(user=user).filter(status=0)
    return render(request,'player/bookings_inprogress.html',{'Booking_inprogress': bookinginprogress_list})

def delete_confirmedbooking(request,id):
    booking = Booking_inprogress.objects.get(id=id)
    booking.delete()
    return HttpResponseRedirect(reverse('Booking:showconfirmedbookings'))

def delete_bookinginprogress(request,id):
    booking =Booking_inprogress.objects.get(id=id)
    booking.delete()
    return HttpResponseRedirect(reverse('Booking:showbookingsinprogress'))


def show_guests(request):
    user=request.user
    guest_list = User.objects.exclude(id=user.id)
    return render(request,'player/show_guests.html',{'Guest': guest_list})

def addToGame(request,id):
    user=user.request
    booking_inprogress = Booking_inprogress.objects.get(id=id)
    guest = User.objects.get(id=id)
    booking_inprogress.guest = guest
    return HttpResponseRedirect(reverse('Booking:addToGame'))


#def show_booking(request,id):
#    booking = Booking_inprogress.objects.get(id=id)
#    return render(request,'player/show_booking.html',{'Booking': booking })
