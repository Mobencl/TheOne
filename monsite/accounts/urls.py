from django.conf.urls import url
from accounts.views import login_view
from accounts.views import logout_view
from accounts.views import register_view,role_view
from accounts.views import partnerprofile_view, playerprofile_view
from accounts import views
from accounts import forms
from django.conf.urls.static import static
from django.conf import settings



app_name = 'accounts'

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login_view,  name='login'),
    url(r'^role/$', role_view,  name='role'),
    url(r'^logout/$', logout_view,  name='logout'),
    url(r'^register/$', register_view , name='register'),
    url(r'^profile/player/$', playerprofile_view , name='profileplayer'),
    url(r'^profile/partner/$', partnerprofile_view , name='profileplayer'),

    url(r'^profile/partner/$', login_view,  name='profilepartner'),
    url(r'^profile/partner/terrains$', views.terrains_view,  name='terrains'),
    url(r'^profile/partner/terrains/(?P<id>[0-9]+)/delete$', views.deleteTerrain,  name='deleteterrain'),
    url(r'^profile/partner/add$', views.addTerrain,  name='addterrain'),
    url(r'^profile/partner/terrains/(?P<id>[0-9]+)/showavailibility$', views.showAvailibilities,  name='showavailibility'),
    url(r'^profile/partner/terrains/(?P<id>[0-9]+)/addavailibility$', views.addAvailibility,  name='addavailibility')


]
