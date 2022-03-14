
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from adminpanel.models import Admin
from django import forms

class CustomUserCreationFormAdmin(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationFormAdmin, self).__init__(*args, **kwargs)

        for fieldname in ['username','email']:
            self.fields[fieldname].help_text = None
            self.fields['username'].label = "USER NAME"
            self.fields['email'].label = "EMAIL"

    class Meta:
        model = User
        fields = ['username','email'] 



class AdminForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Admin
        fields = ['admin_name','password']