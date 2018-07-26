from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save



class ProfileUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    sportcenterName = models.CharField(max_length=100, default='')
    password = models.CharField(max_length=70,default='')
    role = models.CharField(max_length=255)

class Terrain (models.Model):
    terrainAvailibility =  models.ForeignKey(User,on_delete=models.CASCADE)
    TerrainType = models.CharField(max_length  = 255)
    minimumCapacity = models.IntegerField(default = 0)
    maximumCapacity = models.IntegerField(default = 0)
    Price= models.IntegerField(default = 0)

    class Meta:
        verbose_name_plural = 'Terrain'

class Aivailibility(models.Model):
    availibility = models.ForeignKey(Terrain,on_delete=models.CASCADE)
    opening = models.DateTimeField(default='')
    closing = models.DateTimeField()
    notAvailableFrom= models.DateTimeField()
    notAvailableTill = models.DateTimeField()


    #def __str__(self):
    #    return self.user.username
#def create_profile(sender, **kwargs):
    #if kwargs['created']:
        #user_profile = UserProfile.objects.create(user=kwargs['instance'])



##    first_name = models.CharField(max_length=100, default='')
    #last_name = models.CharField(max_length=100, default='')
#    email = models.EmailField(max_length=70,blank=True)


#post_save.connect(create_profile, sender=User)







##    first_name = models.CharField(max_length=100, default='')
    #last_name = models.CharField(max_length=100, default='')
#    email = models.EmailField(max_length=70,blank=True)
