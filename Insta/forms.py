from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Insta.models import InstaUser, Post


class CustomizedUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=False, label='Prefer Name')
    profile_pic = forms.ImageField(required=False, label='Profile')
    email = forms.EmailField(required=True, label='Email')
    class Meta(UserCreationForm.Meta):
        model = InstaUser
        fields = ('profile_pic','username','email','first_name', 'last_name', 'password1', 'password2')
