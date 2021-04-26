from django.conf.urls import url
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^upload$', views.UploadFileView.as_view(), name="upload"),
    url(r'^error', views.ErrorView.as_view(), name="error"),
    url(r'^success', views.SuccessView.as_view(), name="success"),
    
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#another way to do the static url below
#if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)