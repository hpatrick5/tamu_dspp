import sys

import io
import logging
import os
import pandas as pd
import pickle
from datetime import datetime
from django.contrib.auth.models import User
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models


logger = logging.getLogger(__name__)


def pl_zero_case(value):
    if value == 0:
        return 1
    else:
        return value


def get_trained_file(file, file_info, email):
    here = os.path.dirname(os.path.abspath(__file__))

    model_file_path = '../../ml_models/model_new'
    pl_ranges_file_path = '../../ml_models/performance_label_ranges.csv'
    accepted_csv_cols = ['LocalId', 'Grade', 'Ethnicity', 'ECD', 'LEP', 'SpEd', 'BM 1', 'BM 2']

    filename = os.path.join(here, model_file_path)
    model = pickle.load(open(filename, "rb"))

    data = pd.read_csv(file)
    data.drop(columns=[col for col in data if col not in accepted_csv_cols], inplace=True)

    original_file = data.drop(['LocalId'], axis=1)

    data = data.fillna(data.mean())

    data = pd.get_dummies(data, columns=['Ethnicity'])
    data = data.drop(['LocalId', 'Grade'], axis=1)

    prediction = model.predict(data)
    output = pd.DataFrame(prediction)

    output[0] = round(output[0])

    pl_ranges_filename = os.path.join(here, pl_ranges_file_path)
    pl_ranges_csv = pd.read_csv(pl_ranges_filename)

    index_names = pl_ranges_csv["Grade_Subject"]
    pl_ranges_csv = pl_ranges_csv.drop("Grade_Subject", axis=1)
    pl_ranges_csv.index = index_names

    pl_range_select = pl_ranges_csv.filter(like=file_info, axis=0)
    pl_thresholds = pl_range_select.values.tolist()

    percent_to_next_pl = []
    percent_to_previous_pl = []

    performance_labels = []
    for score in output[0]:
        if score > pl_thresholds[0][2]:
            performance_labels.append("Masters")
            percent_to_next_pl.append(0)
            percent_to_previous_pl.append(abs(score - pl_thresholds[0][2]))

        elif pl_thresholds[0][1] < score <= pl_thresholds[0][2]:
            performance_labels.append("Meets")
            percent_to_next_pl.append(pl_zero_case(abs(score - pl_thresholds[0][2])))
            percent_to_previous_pl.append(pl_zero_case(abs(score - pl_thresholds[0][1])))

        elif pl_thresholds[0][0] < score <= pl_thresholds[0][1]:
            performance_labels.append("Approaches")
            percent_to_next_pl.append(pl_zero_case(abs(score - pl_thresholds[0][1])))
            percent_to_previous_pl.append(pl_zero_case(abs(score - pl_thresholds[0][0])))

        else:
            performance_labels.append("Did Not Meet")
            percent_to_next_pl.append(pl_zero_case(abs(score - pl_thresholds[0][0])))
            percent_to_previous_pl.append(0)

    # Adds results as a column
    original_file['Predicted % Score'] = output[0]
    original_file['Predicted PL'] = performance_labels
    original_file['% to Next PL'] = percent_to_next_pl
    original_file['% to Previous PL'] = percent_to_previous_pl

    s_buf = io.StringIO()
    original_file.index.name = "LocalId"
    trained_csv = original_file.to_csv(path_or_buf=s_buf, mode="w", header=True, index=True)

    date_now = datetime.now()
    date_now = date_now.strftime("%m-%d-%Y_%H:%M:%S")
    fname = str(email) + "_" + str(date_now) + ".csv"

    return InMemoryUploadedFile(s_buf,
                                'file',
                                fname,
                                'application/vnd.ms-excel',
                                sys.getsizeof(trained_csv), None)


class FileInfo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="file_owner")
    document_id = models.CharField(max_length=50)
    original_file_name = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)
