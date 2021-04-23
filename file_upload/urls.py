from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^upload$', views.UploadView.as_view(), name="upload"),
    url(r'^error', views.ErrorView.as_view(), name="error"),
    url(r'^success', views.SuccessView.as_view(), name="success"),
]
