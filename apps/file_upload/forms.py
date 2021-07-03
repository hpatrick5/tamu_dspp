from django import forms
from django.contrib.auth import get_user_model

from .models import File


User = get_user_model()


class UploadFileModelForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('owner', 'subject', 'grade', 'upload_file')
        exclude = ['owner']
