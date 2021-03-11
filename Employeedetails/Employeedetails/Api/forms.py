from django.core import validators
from django import forms
from .models import Data
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class Employee(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['first_name','last_name','company_name','email_id','phone_number','password','confirm_password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'company_name': forms.TextInput(attrs={'class':'form-control'}),
            'email_id': forms.EmailInput(attrs={'class':'form-control'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            'confirm_password': forms.PasswordInput(attrs={'class':'form-control'}),

        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['first_name','last_name','phone_number']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            
            'phone_number': forms.TextInput(attrs={'class':'form-control'}),
            

        }

