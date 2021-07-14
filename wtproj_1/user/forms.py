from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'lname'}),
            'username': forms.TextInput(attrs={'class': 'username'}),
            'email':forms.TextInput(attrs={'class': 'email'}),
            'password1':forms.TextInput(attrs={'class': 'password1'}),
            'password2':forms.TextInput(attrs={'class': 'password2'}),
        }