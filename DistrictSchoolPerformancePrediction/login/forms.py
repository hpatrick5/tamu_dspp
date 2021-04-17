from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#class UploadFileForm(forms.ModelForm):
class UploadFileForm(forms.Form):
    #title = forms.CharField(max_length=50)
    #make an instruction field to say "please upload file"
    file = forms.FileField()


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
