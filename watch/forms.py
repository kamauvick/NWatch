from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile, Business, Neighbourhood, Post, EmergencyContact


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'profile_pic', 'age', 'contact', 'address', 'estate']


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'description', 'location', 'owner']


class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ['name', 'location', 'image']


class EmergencyForm(forms.ModelForm):
    class Meta:
        model = EmergencyContact
        fields = ['name', 'contact', 'description']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tag']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('name', 'estate')
