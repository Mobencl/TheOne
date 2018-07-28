from django import forms
from django.contrib.auth import (authenticate,
     get_user_model,
     login,
     logout,)
from django.contrib.auth.models import User
from accounts.models import Terrain

class AddTerrainView(forms.ModelForm):
    TerrainType= forms.CharField(label ='Terrain Type',
    max_length = 255,
    min_length = 5,
    widget = forms.TextInput(attrs = {'class':'form-control'}))
    minimumCapacity = forms.IntegerField(label='Minimum capacity',widget=forms.TextInput(attrs = {'class':'form-control'}))
    maximumCapacity = forms.IntegerField(label='Maximum capacity',widget=forms.TextInput(attrs = {'class':'form-control'}))
    class Meta:
        model = Terrain
        fields = (
            'TerrainType',
            'minimumCapacity',
            'maximumCapacity',
            'photo'
        )







class PartnerRegisterForm(forms.ModelForm):
    username = forms.CharField(
        label ='Username',
        max_length = 100,
        min_length = 5,
        widget = forms.TextInput(attrs = {'class':'form-control'}))



    sportcenterName = forms.CharField(
    label ='Sportcenter Name',
    max_length = 100,
    min_length = 5,
    widget = forms.TextInput(attrs = {'class':'form-control'}))




    email = forms.EmailField(widget = forms.TextInput(attrs = {'class':'form-control'}))


    password = forms.CharField(
    label ='Password',
    max_length = 100,
    min_length = 5,
    widget = forms.PasswordInput(attrs = {'class':'form-control'}))

    role = forms.CharField(
    label ='Do you want to be a Partner or a Player? ',
    max_length = 100,
    min_length = 5,
    widget = forms.TextInput(attrs = {'class':'form-control'}))


    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'role',

        )


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(
    label ='Username',
    max_length = 100,
    min_length = 5,
    widget = forms.TextInput(attrs = {'class':'form-control'}))


    role = forms.CharField(
    label ='Do you want to be a Partner or a Player? ',
    max_length = 100,
    min_length = 5,
    widget = forms.TextInput(attrs = {'class':'form-control'}))

    email = forms.EmailField(widget = forms.TextInput(attrs = {'class':'form-control'}))


    password = forms.CharField(
    label ='Password',
    max_length = 100,
    min_length = 5,
    widget = forms.PasswordInput(attrs = {'class':'form-control'}))


    first_name = forms.CharField(
label ='First name',
max_length = 100,
min_length = 5,
widget = forms.TextInput(attrs = {'class':'form-control'}))
    last_name = forms.CharField(
label ='Last name',
max_length = 100,
min_length = 5,
widget = forms.TextInput(attrs = {'class':'form-control'}))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'role',
        )

class UserLoginForm(forms.Form):
    username =  forms.CharField(label ='username',
    widget = forms.TextInput(attrs = {'class':'form-control'}))
    password = forms.CharField(label ='Password',
    widget = forms.PasswordInput(attrs = {'class':'form-control'}))

    def clean(self,*args,**kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if password and username:
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.ValidationError("This user is no longer active")
            return super(UserLoginForm, self).clean(*args, **kwargs)
