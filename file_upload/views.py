import os

from .models import File, get_trained_file

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.base import ContentFile
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import TemplateView

from file_upload.forms import UploadFileModelForm

from user_profile.models import UserProfile


ACCEPTED_FILE_TYPES = ['csv']  # for upload


class UploadFileView(TemplateView, LoginRequiredMixin):
    template_name = "file_upload/upload.html"

    def post(self, request, *args, **kwargs):
        context = {"upload_file_form": UploadFileModelForm(
            instance=request.user.user_profile)}

        upload_file_form = UploadFileModelForm(request.POST, request.FILES)

        if upload_file_form.is_valid():
            temp = upload_file_form.save(commit=False)
            temp.grade = request.POST["grade"]
            temp.upload_file = request.FILES["upload_file"]

            file_type = temp.upload_file.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in ACCEPTED_FILE_TYPES:
                return render(request, 'file_upload/error.html')

            trained_file = get_trained_file(temp.upload_file)
            temp.owner = request.user
            temp.upload_file.save(name='results.csv', content=trained_file)
            temp.save()

            file_path = File.objects.get(pk=temp.pk)
            return render(request, 'file_upload/success.html', {'file_path': file_path})

        messages.error(request, upload_file_form.errors)
        return render(request, self.template_name, context=context)

    def get(self, request, *args, **kwargs):
        username = request.user.user_profile
        initial_data = {
                'subject': 'Math',
                'grade' : '5',
        }

        context = {"upload_file_form": UploadFileModelForm(initial=initial_data)}
        return render(request, self.template_name, context=context)


class ErrorView(TemplateView):
    template_name = "file_upload/error.html"


class SuccessView(TemplateView):
    template_name = "file_upload/success.html"
