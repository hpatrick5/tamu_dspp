from django.urls import path, include

urlpatterns = [
    path(r'accounts/', include('allauth.urls')),
]
