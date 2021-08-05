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
    ranges_file_path = '../../ml_models/score_ranges_2021.csv'

    filename = os.path.join(here, model_file_path)
    model = pickle.load(open(filename, "rb"))

    data = pd.read_csv(file)
    original_file = data

    data = data.fillna(data.mean())
    data = pd.get_dummies(data, columns=['Ethnicity'])

    data = data.drop(['LocalId', 'Grade'], axis=1)

    prediction = model.predict(data)
    output = pd.DataFrame(prediction)

    output[0] = round(output[0])

    ranges_filename = os.path.join(here, ranges_file_path)
    ranges = pd.read_csv(ranges_filename)
    index_names = ranges["Grade_Subject"]
    ranges = ranges.drop("Grade_Subject", axis=1)
    ranges.index = index_names

    row = ranges.filter(like=file_info, axis=0)
    thresholds = row.values.tolist()

    distance_to_next_threshold = []
    distance_to_previous_threshold = []

    mastery_ranges = []
    for x in output[0]:
        if x > thresholds[0][2]:
            mastery_ranges.append("Masters")
            distance_to_next_threshold.append(0)
            distance_to_previous_threshold.append(abs(x - thresholds[0][2]))
        elif thresholds[0][1] < x <= thresholds[0][2]:
            mastery_ranges.append("Meets")
            distance_to_next_threshold.append(abs(x - thresholds[0][2]))
            distance_to_previous_threshold.append(abs(x - thresholds[0][1]))
        elif thresholds[0][0] < x <= thresholds[0][1]:
            mastery_ranges.append("Approaches")
            distance_to_next_threshold.append(abs(x - thresholds[0][1]))
            distance_to_previous_threshold.append(abs(x - thresholds[0][0]))
        else:
            mastery_ranges.append("Did Not Meet")
            distance_to_next_threshold.append(abs(x - thresholds[0][0]))
            distance_to_previous_threshold.append(0)

    # Adds results as a column
    original_file['Predicted % Score'] = output[0]
    original_file['Predicted Mastery Range'] = mastery_ranges
    original_file['% to Next Mastery Range'] = distance_to_next_threshold
    original_file['% to Previous Mastery Range'] = distance_to_previous_threshold

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


