
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  

class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields['username'].label = "USER NAME"
            self.fields['email'].label = "EMAIL"
            self.fields['password1'].label = "PASSWORD"
            self.fields['password2'].label = "CONFIRM PASSWORD"

    class Meta:
        model = User
        fields = ['username','email','password1','password2'] 