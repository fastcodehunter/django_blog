from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

class FormAuthorizationUser(forms.Form):
    username=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)
        




class ModelFormRegistrationsUser(forms.ModelForm):
    username=forms.CharField(max_length=25)
    email=forms.CharField(widget=forms.EmailInput)
    password1=forms.CharField(widget=forms.PasswordInput)
    
    
    class Meta:
        model=User
        fields=['username','email','password1']
        