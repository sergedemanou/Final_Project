from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *




class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields =['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','role']


class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = "__all__"
        exclude = ['profile_id']



class ProjetsForm(forms.ModelForm):
    class Meta:
        model = Projets
        fields = "__all__"
        exclude = ['profile_id']
