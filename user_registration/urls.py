from django.conf.urls import url, include

urlpatterns = [
    path(r'^accounts/', include('allauth.urls')),
]
