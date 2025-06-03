from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from accounts.models import User,Profile

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=User
        fields=('username','email')

class LoginForm(AuthenticationForm):
    class Meta:
        model=User
        fields="__all__"

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('first_name','last_name','phone','address','avatar')
