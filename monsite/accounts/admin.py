from django.contrib import admin
from accounts.models import Terrain,ProfileUser
from accounts.models import Aivailibility,Membership

admin.site.register(Terrain)
admin.site.register(ProfileUser)
admin.site.register(Aivailibility)
admin.site.register(Membership)
