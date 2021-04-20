from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#added for upload file
from .models import User_Profile

class Profile_Form(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = [
        'fname',
        'grade',
        #save_file is another way to save a file to django
        #'save_file',
        
        
        #'lname',
        #'technologies',
        #'email',
        'display_picture'
        ]
###

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

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
