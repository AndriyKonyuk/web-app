from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms



class AuthenticateForm(AuthenticationForm):
    username = forms.CharField(label='User names',
                               widget=forms.widgets.TextInput(attrs={'id': 'inputUser', 'class': 'form-control',
                                                                     'placeholder': 'User name', 'autofocus': '',
                                                                     'name': 'User'}))
    password = forms.CharField(label='Password', widget=forms.widgets.PasswordInput(
        attrs={'id': 'inputPassword', 'class': 'form-control', 'placeholder': 'Password', 'name': 'Password'}))


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(
        attrs={"class": "form-control", 'placeholder': 'Email', "name": "username"}))
    username = forms.CharField(
        widget=forms.widgets.TextInput(attrs={"class": "form-control", 'placeholder': 'Username'}))
    first_name = forms.CharField(
        widget=forms.widgets.TextInput(attrs={"class": "form-control", 'placeholder': 'First Name'}))
    last_name = forms.CharField(
        widget=forms.widgets.TextInput(attrs={"class": "form-control", 'placeholder': 'Last Name'}))
    password1 = forms.CharField(required=True, widget=forms.widgets.PasswordInput(
        attrs={"class": "form-control", 'placeholder': 'Password'}))
    password2 = forms.CharField(required=True, widget=forms.widgets.PasswordInput(
        attrs={"class": "form-control", 'placeholder': 'Password Confirmation'}))

    class Meta:
        fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2', ]
        model = User
