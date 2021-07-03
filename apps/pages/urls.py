from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$|^home$', views.HomePageView.as_view(), name="home"),
    url(r'^about$', views.AboutView.as_view(), name="about"),
]
