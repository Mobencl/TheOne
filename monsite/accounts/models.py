from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class ProfileUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    role = models.CharField(max_length=255,null=True)
    address = models.CharField(max_length=255,null=True)
    phone = models.CharField(max_length = 10,null=True)
    postalcode = models.CharField(max_length=6,null=True)
    sportcenterName = models.CharField(max_length=255,default='')
    photo = models.ImageField(upload_to='user_directory_path',default='',blank=True)
    path= models.CharField(max_length=255,default='user_directory_path')

    #gender = models.CharField(max_length=255,null=True)
@receiver(post_save, sender=User)
def set_user(sender,instance,created,**kwargs):
    if created:
        ProfileUser.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_set(sender,instance,**kwargs):
    instance.profileuser.save()

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


class Membership (models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    partner=models.ForeignKey(ProfileUser, on_delete=models.CASCADE, null=True)
    status= models.IntegerField(default=0)
    membershipNumber=models.CharField(max_length=255,default='',null=True)
    class Meta:
        verbose_name_plural = 'Membership'



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
