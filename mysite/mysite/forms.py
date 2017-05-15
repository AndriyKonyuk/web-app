from django import forms

class RegisterForm(forms.Form):
    user_name = forms.CharField(label='Enter your name', max_length=120,)
    user_email = forms.EmailField()
    user_pass = forms.CharField(widget=forms.PasswordInput())