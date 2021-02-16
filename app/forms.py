from django import forms
from .models import Posts
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['name','image']


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email']