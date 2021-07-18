from django.urls import path, include
from . import views

urlpatterns = [
    path(r'accounts/', include('allauth.urls')),
    path(r'accounts/profile/', views.UserProfileView.as_view(), name="profile"),
    path(r'accounts/profile/files', views.UserFileView.as_view(), name="user_files")
]
