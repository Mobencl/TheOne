from django.db import models
from django.contrib.auth.models import User
from accounts.models import Aivailibility, Terrain
from django.dispatch import receiver
from django.db.models.signals import post_save
from accounts.models import ProfileUser
# Create your models here.




class Booking_inprogress(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    terrain = models.ForeignKey(Terrain, on_delete = models.CASCADE)
    email = models.EmailField(max_length=254)
    bookingFrom = models.DateTimeField(null=True)
    bookingUntil = models.DateTimeField(null=True)
    creation_date= models.DateTimeField(auto_now_add=True)
    booking_id = models.CharField(max_length=254,null=True)
    terraintype = models.CharField(max_length=254)
    status = models.IntegerField(blank=True)
    counter = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = 'Booking_inprogress'

class Guest(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    booking = models.ForeignKey(Booking_inprogress, on_delete = models.CASCADE, null=True)
    status = models.IntegerField(default=3)
    class Meta:
        verbose_name_plural = 'Guest'
class Counter(models.Model):
    guest=models.ForeignKey(Guest,on_delete=models.CASCADE)
    counter=models.IntegerField(default=0)
    profile=models.ForeignKey(ProfileUser,on_delete=models.CASCADE,null=True)
