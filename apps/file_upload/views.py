import requests

from .models import File_Info, get_trained_file

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

from apps.file_upload.forms import FileForm

FILE_MANAGER_URL = "http://54.160.87.107:5000/doc"

class UploadFileView(TemplateView, LoginRequiredMixin):
    template_name = "pages/upload.html"

    def post(self, request, *args, **kwargs):
        context = {"file_form": FileForm()}
        form = FileForm(request.POST, request.FILES)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            grade = form.cleaned_data['grade']
            file = request.FILES['file']

            # file type check
            file_type = file.name.split('.')[-1]
            file_type = file_type.lower()
            # ADD SIZE RESTRICTION
            if file_type != 'csv':
                messages.warning(request, 'Oops! Something went wrong with the file upload. Please check your CSV '
                                          'file and make sure it is in the correct format.')
                return HttpResponseRedirect('upload')

            # ML train
            # file = get_trained_file(file)
            trained_file = {'document': file }
            payload = {
                'user_email': request.user.username.__str__,
            }

            r = requests.post(FILE_MANAGER_URL, files=trained_file, data=payload)

            if r.status_code != 200:
                messages.warning(request, 'Oops! Something went wrong with the file upload.' + r.status_code + ' ' + r.content)
                return HttpResponseRedirect('upload')

            file_info = File_Info()

            file_info.owner = request.user
            file_info.document_id = r.json()['document_id']
            file_info.original_file_name = file.name
            file_info.grade = grade
            file_info.subject = subject

            file_info.save()

            # temp file?
            # file_path = File.objects.get(pk=temp.pk)
            # get request to file
            # warning: file download here is temporary - go to my files page to see all files after this
            return render(request, 'pages/upload_success.html', {'file_path': FILE_MANAGER_URL + "/" + file_info.document_id})

        messages.error(request, form.errors)
        return render(request, self.template_name, context=context)

    def get(self, request, *args, **kwargs):
        # username = request.user_display_user
        initial_data = {
                'subject': 'Math',
                'grade' : '5',
        }

        context = {"file_form": FileForm(initial=initial_data)}
        return render(request, self.template_name, context=context)


class SuccessView(TemplateView):
    template_name = "pages/upload_success.html"
