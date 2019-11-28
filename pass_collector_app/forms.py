from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Passwords

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields = ['username', 'email', 'password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class AddPassword(forms.ModelForm):

    class Meta:
        model = Passwords
        # sourse_name = forms.CharField(label='Sourse Name')
        # link_to_site = forms.CharField(label='Link To Source')
        # user_login = forms.CharField(label='Login')
        # user_password = forms.CharField(label='Password')
        fields = ['sourse_name', 'link_to_site', 'user_login', 'user_password', ]
        labels = {
            'sourse_name': 'Sourse Name',
            'link_to_site': 'Link To Source',
            'user_login': 'Login',
            'user_password': 'Password'
        }
        required = {
            'user_password': False

        }
