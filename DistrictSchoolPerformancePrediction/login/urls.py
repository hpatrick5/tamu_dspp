from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='login-home'),
    path('about/', views.about, name='login-about'),
    path('upload/', views.upload_file, name='login-upload'),
    path('register/', views.register, name='register')
]
