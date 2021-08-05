import logging
import os
import sys
import io

import pandas as pd
import pickle

from django.contrib.auth.models import User
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models

logger = logging.getLogger(__name__)


def get_trained_file(file, grade, subject):
    
    here = os.path.dirname(os.path.abspath(__file__))

    file_info = subject.lower() + "_" + grade
    # model_file_path = ('../../ml_models/' + grade+'_'+subject.lower())
    model_file_path = '../../ml_models/model_new'
    filename = os.path.join(here, model_file_path)
    model = pickle.load(open(filename, "rb"))

    data = pd.read_csv(file)
    original_file = data

    data = data.fillna(data.mean())
    data = pd.get_dummies(data, columns=['Ethnicity'])

    data = data.drop(['LocalId', 'Grade'], axis=1)

    prediction = model.predict(data)
    output = pd.DataFrame(prediction)

    # Adds results as a column
    original_file['Predicted % Score'] = output[0]
    s_buf = io.StringIO()
    trained_csv = original_file.to_csv(path_or_buf=s_buf, mode="w", header=True)
    
    return InMemoryUploadedFile(s_buf,
                                   'file',
                                   'trained_csv.csv',
                                   'application/vnd.ms-excel',
                                   sys.getsizeof(trained_csv), None)


class File_Info(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="file_owner")
    document_id = models.CharField(max_length=50)
    original_file_name = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)


