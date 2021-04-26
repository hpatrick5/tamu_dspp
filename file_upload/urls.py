from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views


urlpatterns = [
    url(r'^upload$', views.UploadFileView.as_view(), name="upload"),
    url(r'^error', views.ErrorView.as_view(), name="error"),
    url(r'^success', views.SuccessView.as_view(), name="success"),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
