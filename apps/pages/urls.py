from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$|^home$', views.HomePageView.as_view(), name="home"),
    url(r'^about$', views.AboutView.as_view(), name="about"),
    url(r'^file_info$', views.FileInformationView.as_view(), name="file_info"),
    url(r'^download/(?P<path>.*)$', views.TestProxyView.as_view()),
    url(r'^why_use', views.WhyUseView.as_view(), name="why_use"),
    url(r'^results_explained', views.ResultsExplainedView.as_view(), name="results_explained"),
]
