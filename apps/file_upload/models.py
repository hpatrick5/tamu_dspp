import logging
import os
import pandas as pd
import pickle

from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from django.db import models

logger = logging.getLogger(__name__)


def get_trained_file(self):
    # choose correct model
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, '../../ml_models/5_math')
    model = pickle.load(open(filename, "rb"))

    math = pd.read_csv(self)
    math = math.fillna(math.mean())
    math = pd.get_dummies(math, columns=['Ethnicity'])

    responseVariable = 'Spring 2019 STAAR\nMA05\nPcntScore\n5/2019 or 6/2019'
    math_analysis = math.iloc[:, 2:]
    x_math = math_analysis.drop(responseVariable, axis=1)

    prediction = model.predict(x_math)
    output = pd.DataFrame(prediction)
    return ContentFile(output.to_csv(index=False, header=True))


class File_Info(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="file_owner")
    document_id = models.CharField(max_length=50)
    original_file_name = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)


