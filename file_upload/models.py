import logging
import os

from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from django.utils import timezone


logger = logging.getLogger(__name__)


def upload_file_to(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return 'userprofile/%s%s' % (
        timezone.now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),
    )


class File(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="file_owner")
    grade = models.PositiveIntegerField()
    upload_path = u'uploads/%Y/%m/%d/'
    
    #look at blank = true or not in django documentation 
    upload_file = models.FileField(
        default=None, verbose_name="file_name", upload_to=upload_path, null=True, blank=True)
    
    def __str__(self):
        return str(self.upload_file)


class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ['owner','grade','upload_file']