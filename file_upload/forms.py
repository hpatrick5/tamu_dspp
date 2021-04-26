from django import forms
from django.contrib.auth import get_user_model
from .models import File


User = get_user_model()


class UploadFileModelForm(forms.ModelForm):
    class Meta:
        model = File
        #need a user field, title field?
        fields = ('owner', 'grade', 'upload_file')
        exclude = ['owner']