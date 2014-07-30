from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
class LoginForm(forms.Form):
    username = forms.CharField(label=(u'User Name'))
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))

    def clean(self):
        username=self.cleaned_data['username']
        password=self.cleaned_data['password']

        if username and password:
            self.usr=authenticate(username=username,password=password)

            if self.usr is None:
                raise forms.ValidationError("The User Does Not Exist")
            else:
                self.confirm_login_allowed(self.usr)
        return self.cleaned_data

    def confirm_login_allowed(self,usr):
        if not usr.is_active:
            raise forms.ValidationError("User is Inactive")