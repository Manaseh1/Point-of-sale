from django import forms 
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from accounts.models import NewEmployee,Profile


class EmployeeCreationForm(forms.ModelForm):
      class Meta:
         model = NewEmployee
         fields = ('username','role','email')

class EmployeeEditForm(forms.ModelForm):
      class Meta:
         model = NewEmployee
         fields = ('username','first_name','last_name','role','email')
         