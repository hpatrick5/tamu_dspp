from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#added for upload file
from .models import User_Profile, SavedFile

class Profile_Form(forms.ModelForm):
    class Meta:
        model = SavedFile
        # model = User_Profile
        fields = [
        # 'first_name',
        # 'grade',
        #save_file is another way to save a file to django
        #'save_file',
        #'lname',
        #'technologies',
        #'email',
        'upload_file'
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
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
