from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.base import ContentFile
from django.shortcuts import render
from django.views.generic import TemplateView

from file_upload.forms import UploadFileModelForm

#used to downlaod files
import os
from django.conf import settings
from django.http import HttpResponse, Http404

from .models import File, get_trained_file
from user_profile.models import UserProfile

from dspp.settings import BASE_DIR,MEDIA_ROOT, MEDIA_URL
## end of download files


# accepted file types for upload
ACCEPTED_FILE_TYPES = ['csv']


class UploadFileView(TemplateView, LoginRequiredMixin):
    template_name = "file_upload/upload.html"

    def post(self, request, *args, **kwargs):
        # context = super(UploadFileView(), self).get_context_data(**kwargs)
        # context['upload_file_form'] = upload_file_form = UploadFileModelForm(
        #           request.POST, request.FILES, instance=request.user.user_profile)

        #might be able to delete line directly below comments as its useless with understanding of context
        #context will only be pushed to page when error
        context = {"upload_file_form": UploadFileModelForm(
            instance=request.user.user_profile)}

        upload_file_form = UploadFileModelForm(request.POST, request.FILES)
        
        ##csv file type confirmation
        if upload_file_form.is_valid():
            temp02 = upload_file_form.save(commit=False)
            temp02.upload_file = request.FILES["upload_file"]
            file_type = temp02.upload_file.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in ACCEPTED_FILE_TYPES:
                return render(request, 'file_upload/error.html')
        ##
        
        
        if upload_file_form.is_valid():
            temp = upload_file_form.save(commit=False)
            temp.grade = request.POST["grade"]
            temp.upload_file = request.FILES["upload_file"]
            trained_file = get_trained_file(temp.upload_file)
            temp.owner = request.user
            temp.upload_file.save(name='results.csv',content=trained_file)
            temp.save()
            
            file_path = File.objects.get(pk=temp.pk)
            return render(request, 'file_upload/success.html', {'file_path': file_path})

        messages.error(request, upload_file_form.errors)
        return render(request, self.template_name, context=context)

    # get will be when form is empty, just going to that page
    def get(self, request, *args, **kwargs):
        # context = super(UploadFileView(), self).get_context_data(**kwargs)

        username = request.user.user_profile
        initial_data = {
                'grade' : 5,
        }

        # context = {"upload_file_form": UploadFileModelForm(
        #     instance=request.user.user_profile)}

        context = {"upload_file_form": UploadFileModelForm(initial=initial_data)}

        # context['user_detail_form'] = UserDetailModelForm(
        #     instance=request.user)
        return render(request, self.template_name, context=context)

class ErrorView(TemplateView):
    template_name = "file_upload/error.html"


class SuccessView(TemplateView):
    template_name = "file_upload/success.html"
