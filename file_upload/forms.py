from django import forms
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


from .models import File
# added for upload file
#from .models import User_Profile

#legacy code
#from user_profile.models import UserProfile
##

#with form I need a model, and the view has to call this form
class UploadFileModelForm(forms.ModelForm):
    class Meta:
        model = File
        #need a user field, title field?
        fields = ('owner', 'grade', 'upload_file')