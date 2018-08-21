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
from accounts.models import ProfileUser, Aivailibility, Membership
from accounts.forms import UserRole, MembershipForm
from Booking.models import Guest


def home (request):
    return render(request,"accounts/home.html")

def login_view(request):
    form = UserLoginForm(request.POST or None )
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if user.profileuser.role == 'Player':
            return redirect('/account/profile/player/')
        elif user.profileuser.role =='Partner':
            return redirect('/account/profile/partner/')
    return render(request,'accounts/login.html',{'form': form})


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
        return redirect('/account/role/')
    return render(request,'accounts/register_form.html',{'form': form})


def role_view(request):
    form=UserRole(request.POST or None)
    if form.is_valid:
        user=request.user
        role=request.POST.get('role')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        user.profileuser.role=role
        user.profileuser.address = address
        user.profileuser.phone = phone
        user.save()
        if  user.profileuser.role == 'Partner':
            return redirect ('/account/profile/partner')
        elif user.profileuser.role =='Player':
            return redirect ('/account/profile/player')
    return render(request,'accounts/userrole.html',{'form': form})


#For the player
def show_sportcenters(request):
    user=request.user
    sportcenter_list = ProfileUser.objects.filter(role='Partner')
    return render(request,'membership/show_sportcenters.html',{'ProfileUser': sportcenter_list})


def membership_proposal(request,id):
    user=request.user
    partner=ProfileUser.objects.get(id=id)
    membership= Membership()
    form=MembershipForm(request.POST or None)
    if form.is_valid():

        membership.membershipNumber= form.cleaned_data.get('membership')
        membership.user=user
        membership.partner=partner
        membership.save()
        return HttpResponseRedirect(reverse('accounts:confirmedmembership'))
    return render(request,'membership/add_membership.html',{'form': form})




def confirmed_memberships(request):
    user = request.user
    membership_list=Membership.objects.filter(user=user).filter(status=1)
    inprogressmember_list=Membership.objects.filter(user=user).filter(status=0)
    return render(request,'membership/confirmed_membership.html',{'Membership': membership_list, 'Inprogress': inprogressmember_list})


#For the partner
def show_membershipproposals(request):
    membershipProposal= Membership.objects.filter(status=0)
    return render(request,'membership/show_membershipproposals.html',{'Membership': membershipProposal})

def accept_membershipproposal(request,id):
    membershipProposal=Membership.objects.get(id=id)
    membershipProposal.status=1
    membershipProposal.save()
    return HttpResponseRedirect(reverse('accounts:showmembershipproposals'))

def deny_membership(request,id):
    membershipProposal=Membership.objects.get(id=id)
    membership.status=0
    membershipProposal.save()
    return HttpResponseRedirect(reverse('accounts:showmembershipproposals'))

def partnerconfirmed_membership(request):
    user=request.user
    membership_list=Membership.objects.filter(user=user).filter(status=1)
    return render(request,'membership/show_partnermembership.html',{'Membership': membership_list})


def delete_membership(request,id):
    user=request.user
    memebership=Membership.obejcts.get(id=id)
    membership.delete()
    return HttpResponseRedirect(reverse('accounts:confirmedmembership'))













def partnerprofile_view(request):
    user = request.user
    args = {'user': user}
    return render(request, 'accounts/partnerprofile.html',args)


def playerprofile_view(request):
    user=request.user
    guest_list =Guest.objects.filter(user=user).filter(status=0)

    return render(request,'accounts/playerprofile.html',{'user': user,'Guest': guest_list})


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
        if user.profileuser.role == 'Partner':
            return redirect('/account/profile/partner')
        elif user.profileuser.role == 'Player':
            return redirect('/account/profile/player')
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
