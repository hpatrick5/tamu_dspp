import logging
import os
import pandas as pd
import pickle

from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from django.utils import timezone

logger = logging.getLogger(__name__)


#can probably delete this
def upload_file_to(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return 'userprofile/%s%s' % (
        timezone.now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),
    )


def get_trained_file(self):
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, 'math_7th_pickle')
    model = pickle.load(open(filename, "rb"))

    math = pd.read_csv(self)
    math = math.fillna(math.mean())
    math = pd.get_dummies(math,columns=['Ethnicity'])

    responseVariable = 'Spring 2019 STAAR\nMA05\nPcntScore\n5/2019 or 6/2019'
    math_analysis=math.iloc[:,2:]
    x_math = math_analysis.drop(responseVariable,axis=1)

    prediction = model.predict(x_math)
    output = pd.DataFrame(prediction)
    return ContentFile(output.to_csv(index=False, header=True))


class File(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="file_owner")
    
    READING_ENGLISH = 'RE'
    READING_SPANISH = 'RS'
    MATH = 'MA'
    
    SUBJECT_CHOICES = [(READING_ENGLISH, 'Reading-Spanish'),(READING_SPANISH,'Reading-English'),(MATH, 'Math')]
    
    subject = models.CharField(max_length = 25,
        choices = SUBJECT_CHOICES,
        default = None)
        
    #grade = models.PositiveIntegerField(max_value = 12, min_value = 1)
    grade = models.PositiveIntegerField()
    upload_path = 'uploads/%Y/%m/%d/'

    # look at blank = true or not in django documentation
    upload_file = models.FileField(
        default=None,
        verbose_name="file_name",
        upload_to=upload_path,
        null=True,
        blank=True
    )

    def __str__(self):
        return str(self.upload_file)

    @property
    def upload_file_url(self):
        if self.upload_file and hasattr(self.upload_file, 'url'):
            return(self.upload_file.url)


class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ['owner', 'subject', 'grade', 'upload_file']
