from django.contrib.auth import authenticate
from django.contrib.auth import  login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse
from accounts.forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from accounts.forms import PartnerRegisterForm
from accounts.models import Terrain
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from accounts.forms import AddTerrainView,AvailibilityForm
from accounts.models import ProfileUser, Aivailibility


def home (request):
    return render(request,"accounts/home.html")

def login_view(request):
    form = UserLoginForm(request.POST or None )
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/account/profile/')
    return render(request,'accounts/login.html',{'form': form})


#def partner_register_view(request):
#    form = PartnerRegisterForm(request.POST or None)
#    if form.is_valid():
#        sportcenterNem=form


def register_view(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user =  form.save(commit = False)
        username= form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user.set_password(password)
        user.save()
        new_user = authenticate(username = user.username, password = password)
        login(request, new_user)
        return redirect('/account/profile/player')

    return render(request,'accounts/register_form.html',{'form': form})

def partner_register_view(request):
    form = PartnerRegisterForm(request.POST or None)
    if form.is_valid():
        user =  form.save(commit = False)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username = user.username, password = password)
        login(request, new_user)
        return redirect('/account/profile/partner')

    return render(request,'accounts/register_form.html',{'form': form})

def profile_view(request,pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html',args)

def terrains_view(request):
    user=request.user
    terrains_list=Terrain.objects.filter(terrainAvailibility=user)
    return render(request,'terrains/terrains.html',{'Terrain': terrains_list})
def deleteTerrain(request,id):
    #user=user.request
    terrain=Terrain.objects.get(id=id)
    terrain.delete()
    #terrains_list=Terrain.objects.filter(terrainAvailibility=user)
    #return render(request,'terrains/terrains.html',{'Terrain': terrains_list})
    return HttpResponseRedirect(reverse('accounts:terrains'))



def addTerrain(request):
    user=request.user
    form= AddTerrainView(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            terrain =form.save(commit=False)
            terrain.terrainAvailibility = request.user
            terrain.save()
        return redirect('/account/profile/partner/terrains')

    return render(request,'terrains/addTerrain_form.html',{'form': form})

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


def logout_view(request):
    logout(request)
    form = UserLoginForm(request.POST or None )
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/account/profile/')
    return render(request,'accounts/login.html',{'form': form})


def showAvailibilities(request,id):
    #user=request.user
    terrain = Terrain.objects.get(id=id)
    availibility_list = Aivailibility.objects.filter(availibility=terrain)
    return render(request,'terrains/availibility.html',{'Availibility': availibility_list})

def addAvailibility(request,id):
    user=request.user
    terrain = Terrain.objects.get(id=id)
    #availibility = Aivailibility.objects.get(partner=user)
    form= AvailibilityForm(request.POST or None)
    if request.method =='POST':
        if form.is_valid():
            availibilities = form.save(commit=False)
            availibilities.availibility =  terrain
            availibilities.save()
        return redirect('/account/profile/partner/terrains')

    return render(request,'terrains/addavailibility.html',{'form': form})
