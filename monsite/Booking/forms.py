from django import forms
from django.contrib.auth import (authenticate,
     get_user_model,
     login,
     logout,)
from django.contrib.auth.models import User
from accounts.models import Terrain, Aivailibility
from django.contrib.admin.widgets import AdminSplitDateTime
from Booking.models import Booking_inprogress





class BookingProgress(forms.ModelForm):
    bookingFrom  = forms.SplitDateTimeField(
    label ='From',
    input_time_formats=['%I:%M %p', '%H:%M:%S'],
    widget=AdminSplitDateTime())
    bookingUntil= forms.SplitDateTimeField(
    input_time_formats=['%I:%M %p', '%H:%M:%S'],
    widget=AdminSplitDateTime(),
    label ='Until')
    class Meta:
        model = Booking_inprogress
        fields = (
            'bookingFrom',
            'bookingUntil',
            )
    def clean(self,*args,**kwargs):
        bookingFrom = self.cleaned_data.get('bookingFrom')
        bookingUntil = self.cleaned_data.get('bookingUntil')
        if bookingFrom.date()  !=  bookingUntil.date():
            raise forms.ValidationError('Your reservation should have the same date')
        if bookingFrom.time() == bookingUntil.time():
            raise forms.ValidationError('You cannot choose the same time for the begining and the end of the game')
        return super(BookingProgress, self).clean(*args, **kwargs)
        
