import sys

import boto3
import io
import logging
import os
import pandas as pd
import pickle
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def aws_session():
    """
    Authenticates in to the S3 bucket to upload and download CSV files. This step is necessary to access the files in
    the S3 bucket. Note: only authenticated users or this website is able to access the files in the bucket. No
    outside user can plug in the URL to get the files.

    :return: Authenticated AWS session connecting to the S3 bucket
    """
    return boto3.session.Session(aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                                 aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                                 region_name=os.getenv('AWS_REGION_NAME'))


def get_s3_path(user):
    """
    Determines the path where the CSV file will be placed in the S3 bucket.

    :param user: username of who is uploading the file
    :return: folder path based on username and date
    """
    date_now = datetime.now()

    day = date_now.day
    month = date_now.month
    year = date_now.year

    path = "uploads/" + str(user) + "/" + str(year) + "/" + str(month) + "/" + str(
        day) + "/"

    return path


def upload_data_to_bucket(file, user):
    path = os.path.join(get_s3_path(user), file.name)
    session = aws_session()
    s3_resource = session.resource('s3')
    obj = s3_resource.Object(os.getenv('AWS_STORAGE_BUCKET_NAME'), path)
    obj.put(ACL='private', Body=file.read())
    return path


@login_required(login_url='/accounts/login/')
def download_data_from_bucket(request, path):
    session = aws_session()
    s3_resource = session.resource('s3')
    obj = s3_resource.Object(os.getenv('AWS_STORAGE_BUCKET_NAME'), path)
    io_stream = io.BytesIO()
    obj.download_fileobj(io_stream)

    io_stream.seek(0)
    data = io_stream.read().decode('utf-8')

    response = HttpResponse(data, content_type="text/csv")
    response['Content-Disposition'] = "attachment;filename=" + path.split("/")[-1]
    return response


def pl_zero_case(value):
    if value == 0:
        return 1
    else:
        return value


def get_trained_file(file, file_info, email):
    here = os.path.dirname(os.path.abspath(__file__))

    model_file_path = '../../ml_models/model_new'
    pl_ranges_file_path = '../../ml_models/performance_label_ranges.csv'
    accepted_csv_cols = ['Numerical Identifier', 'Grade', 'Ethnicity', 'ECD', 'LEP', 'SpEd', 'BM 1', 'BM 2']

    filename = os.path.join(here, model_file_path)

    model_open = open(filename, "rb")
    model = pickle.load(model_open)
    model_open.close()

    data = pd.read_csv(file)
    data.drop(columns=[col for col in data if col not in accepted_csv_cols], inplace=True)

    original_file = data.drop(['Numerical Identifier'], axis=1)

    data = data.fillna(data.mean())

    data = pd.get_dummies(data, columns=['Ethnicity'])
    data = data.drop(['Numerical Identifier', 'Grade'], axis=1)

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

    s_buf = io.BytesIO()
    original_file.index.name = "Numerical Identifier"
    trained_csv = original_file.to_csv(path_or_buf=s_buf, mode="wb", encoding="UTF-8", header=True, index=True)
    s_buf.seek(0)

    date_now = datetime.now()
    date_now = date_now.strftime("%m-%d-%Y_%H:%M:%S")
    fname = str(email) + "_" + str(date_now) + ".csv"

    return InMemoryUploadedFile(s_buf,
                                'file',
                                fname,
                                'application/vnd.ms-excel',
                                sys.getsizeof(trained_csv), None)
