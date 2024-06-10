from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'user_type')

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
