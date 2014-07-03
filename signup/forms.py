from django import forms
from django.contrib.auth.models import User
from models import Registration
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext, ugettext_lazy as _
import random

class Signup(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name =forms.CharField(required=True)
    last_name = forms.CharField(required=True)



    class Meta:
        model = User
        fields= ('first_name','last_name','username','email','password1','password2')



    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False
        if commit:
            user.save()
        return user