from django.db import models
from django.contrib.auth.models import User
from accounts.models import Aivailibility, Terrain
from django.dispatch import receiver
from django.db.models.signals import post_save
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
    class Meta:
        verbose_name_plural = 'Booking_inprogress'
