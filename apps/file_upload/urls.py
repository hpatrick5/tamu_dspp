from apps.file_upload.utils import download_data_from_bucket
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^upload$', views.UploadFileView.as_view(), name="upload"),
    url(r'^download/(?P<path>.*)$', download_data_from_bucket, name="download_data_from_bucket"),
]

