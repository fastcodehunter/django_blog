from django import forms
from django.contrib.auth.models import User


class FormAuthorizationUser(forms.Form):
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'input__form'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input__form'})) 




class ModelFormRegistrationsUser(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'input__form'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'input__form'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input__form'}))
    
    
    class Meta:
        model=User
        fields=['username','email','password1']
        