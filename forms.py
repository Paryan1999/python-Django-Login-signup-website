
from django.contrib.auth.models import User
from.models import Profile
from django import forms
class Profile_forms(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['name','address','p_img']


# from django.contrib.auth.forms import UserCreationForm

# class UserRegistrationForm(UserCreationForm):
#     email=forms.EmailField()
#     class Meta:
#         model=User
#         fields=['username','email','password1','password2']

# class UserUpdationForm(forms.ModelForm):