from django.views.generic import TemplateView


# Create your views here.

class UploadView(TemplateView):
    template_name = "file_upload/upload.html"

class ErrorView(TemplateView):
    template_name = "file_upload/error.html"

class SuccessView(TemplateView):
    template_name = "file_upload/success.html"