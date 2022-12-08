from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    """
    This Meta class specifies the model the form should interact with
    model = User because whenever this form validates, it's going to create a new user
    fields list are the fields that are going to be show in the form, in the specified order
    """
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class UserUpdateForm(forms.ModelForm): 
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email"]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
            model = Profile
            fields = ["image"]
