from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm) :
    class Meta :
        model = User
        help_texts = {
            'username' : None,
        }
        widgets = {
            'password' : forms.PasswordInput()
        }
        fields = ['username', 'email', 'password']

class LoginForm(forms.ModelForm) :
    class Meta :
        model = User
        help_texts = {
            'username' : None,
        }
        widgets = {
            'password' : forms.PasswordInput()
        }
        fields = ['username', 'password']
