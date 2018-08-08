from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from time import strftime


class ProfileUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    sportcenterName = models.CharField(max_length=100, default='')
    #password = models.CharField(max_length=70,default='')
    role = models.CharField(max_length=255,default='')
    photo = models.ImageField(upload_to='user_directory_path',default='')
class Terrain (models.Model):
    terrainAvailibility =  models.ForeignKey(User,on_delete=models.CASCADE)
    TerrainType = models.CharField(max_length  = 255)
    minimumCapacity = models.IntegerField(default = 0)
    maximumCapacity = models.IntegerField(default = 0)
    Price= models.IntegerField(default = 0)
    photo = models.ImageField(upload_to='user_directory_path',default='')
    path= models.CharField(max_length=255,default='user_directory_path')
    class Meta:
        verbose_name_plural = 'Terrain'
class Aivailibility(models.Model):
    availibility = models.ForeignKey(Terrain,on_delete=models.CASCADE)
    #partner = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    opening = models.DateTimeField(null=True)
    closing = models.DateTimeField(null=True)
    notAvailableFrom= models.DateTimeField(null=True)
    notAvailableTill = models.DateTimeField(null=True)
    class Meta:
        verbose_name_plural = 'Aivailibility'

    #def From(self):
    #    return self.strftime("%Y-%m-%d %H:%M:%S",self.notAivalableFrom)
    #def Begin(self):
    #        return self.strftime("%Y-%m-%d %H:%M:%S",self.opening)
    #def End(self):
    #        return self.strftime("%Y-%m-%d %H:%M:%S",self.closing)
    #def Till(self):
    #    return self.strftime("%Y-%m-%d %H:%M:%S".self.notAvaialableTill)




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
