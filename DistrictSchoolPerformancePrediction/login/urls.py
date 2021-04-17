from django.urls import path
from . import views

#added this for upload files
#from myproject import settings
#from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name='login-home'),
    path('about/', views.about, name='login-about'),
    path('upload/', views.upload_file, name='login-upload'),
    path('register/', views.register, name='register')
    
    #added for file upload
    #path('', views.create_profile, name = 'create')
]
