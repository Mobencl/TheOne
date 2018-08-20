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
from Booking.models import Booking_inprogress, Guest
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

def confirm_booking(request,id):#chaneg the status of the booking to
    pass
    #user=request.user
    #new_availibility = Aivailibility()
    #new_availibility.notAvailableFrom= booking_inprogress.bookingFrom
    #new_availibility.notAvailableTill= booking_inprogress.bookingUntil
    #new_availibility.availibility= booking_inprogress.terrain
    #new_availibility.save()
    #Confirmed booking the default 0 is for a booking in progress
    #return render(request,'player/show_booking.html',{'Booking_inprogress': booking_inprogress})

def show_confirmedbookings(request):
    user=request.user
    confirmedbooking_list = Booking_inprogress.objects.filter(user=user).filter(status=1)
    return render(request,'player/confirmed_bookings.html',{'Booking_inprogress': confirmedbooking_list})

def show_bookingsinprogress(request):
    user=request.user
    bookinginprogress_list = Booking_inprogress.objects.filter(user=user).filter(status=0)
    inprogressguest_list = Guest.objects.filter(user=user).filter(status=1)
    return render(request,'player/bookings_inprogress.html',{'Booking_inprogress': bookinginprogress_list, 'Guest': inprogressguest_list })

def delete_confirmedbooking(request,id):
    booking = Booking_inprogress.objects.get(id=id)
    booking.delete()
    return HttpResponseRedirect(reverse('Booking:showconfirmedbookings'))

#I should add a function so the guest can cancel his booking in a guest_list/status =  or delete the Guest from the database

def delete_bookinginprogress(request,id):
    booking =Booking_inprogress.objects.get(id=id)
    guest_list= Guest.objects.filter(booking=booking)
    guest_list.delete()
    booking.delete()
    return HttpResponseRedirect(reverse('Booking:showbookingsinprogress'))


def show_guests(request):
    user=request.user
    role=user.profileuser.role
    guest_list = ProfileUser.objects.exclude(id=user.id).filter(role='Player')
    return render(request,'player/show_guests.html',{'ProfileUser': guest_list})

def add_guests(request,id):
    user=request.user
    booking_inprogress = Booking_inprogress.objects.get(user=user)#there is only one booking in progress
    profileUser = ProfileUser.objects.get(id=id)
    newGuest = Guest()
    newGuest.booking=booking_inprogress
    newGuest.user=profileUser.user
    newGuest.save()
    return HttpResponseRedirect(reverse('Booking:showguests'))




def accept_proposal(request,id):
    guest = Guest.objects.get(id=id)
    guest.status = 1
    #counter=guest.booking.counter
    #booking = guest.booking
    #counter+=1
    #booking.counter = counter
    #booking.save()
    guest.save()
    return HttpResponseRedirect(reverse('Booking:confirm'))

def decline_proposal(request,id):
    guest =  Guest.objects.get(id=id)
    guest.delete()
    return HttpResponseRedirect(reverse('account:playerprofile'))



#def decline_proposal(request,id):
    #booking_proposal = Booking_inprogress.objects.get(id=id)
    #

#def acceptGame
#booking_inprogress.guest.status

#def show_booking(request,id):
#    booking = Booking_inprogress.objects.get(id=id)
#    return render(request,'player/show_booking.html',{'Booking': booking })
