from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^upload$', views.UploadFileView.as_view(), name="upload"),
]

