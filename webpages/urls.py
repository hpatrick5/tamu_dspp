from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name="homepage"),
    url(r'^terms$', views.TermsView.as_view(), name="terms"),
    url(r'^about$', views.AboutView.as_view(), name="about"),
    url(r'^home', views.HomePageView.as_view(), name="home"),
]
