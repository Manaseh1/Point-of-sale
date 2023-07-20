# from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,NewEmployee

class SignupForm(UserCreationForm):
    class Meta:
        model = NewEmployee
        fields = ('username','email','password1','password2')
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None    
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'first_name', 'last_name', 'address', 'city', 'profile_image',
                  'date_of_birth', 'gender', 'role']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = NewEmployee
        fields = ('username','email')