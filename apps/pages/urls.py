from django.conf.urls import url

from . import views
from apps.file_upload.utils import download_data_from_bucket


urlpatterns = [
    url(r'^$|^home$', views.HomePageView.as_view(), name="home"),
    url(r'^about$', views.AboutView.as_view(), name="about"),
    url(r'^file_info$', views.FileInformationView.as_view(), name="file_info"),
    url(r'^download/(?P<path>.*)$', views.download_data_from_bucket, name="download_data_from_bucket"),
    url(r'^why_use', views.WhyUseView.as_view(), name="why_use"),
    url(r'^results_explained', views.ResultsExplainedView.as_view(), name="results_explained"),
]
