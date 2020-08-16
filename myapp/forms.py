from django import forms
from myapp.models import *

class RegisterUserForm(forms.ModelForm):
    class Meta:
         model = RegisterUser
         fields = "__all__"