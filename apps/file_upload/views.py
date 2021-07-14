from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import File, get_trained_file

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

from apps.file_upload.forms import UploadFileModelForm

ACCEPTED_FILE_TYPES = ['csv']  # for upload


class UploadFileView(TemplateView, LoginRequiredMixin):
    template_name = "pages/upload.html"

    def post(self, request, *args, **kwargs):
        context = {"upload_file_form": UploadFileModelForm(
            )}

        upload_file_form = UploadFileModelForm(request.POST, request.FILES)

        if upload_file_form.is_valid():
            temp = upload_file_form.save(commit=False)
            temp.grade = request.POST["grade"]
            temp.subject = request.POST["subject"]
            temp.upload_file = request.FILES["upload_file"]

            file_type = temp.upload_file.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in ACCEPTED_FILE_TYPES:
                messages.warning(request, 'Oops! Something went wrong with the file upload. Please check your CSV file and make sure it is in the correct format.')
                return HttpResponseRedirect('upload')
            
            #gets trained data calling def get_trained_file in models.py
            #upload_file, temp.grade, temp.subject)
            trained_file = get_trained_file(temp)
            temp.owner = request.user
            if trained_file == None:
                messages.warning(request, 'Oops! Something went wrong with the file upload. Please check your CSV file and make sure it is in the correct format.')
                return HttpResponseRedirect('upload')
            temp.upload_file.save(name='results.csv', content=trained_file)
            temp.save()

            file_path = File.objects.get(pk=temp.pk)
            return render(request, 'pages/upload_success.html', {'file_path': file_path})

        messages.error(request, upload_file_form.errors)
        return render(request, self.template_name, context=context)

    def get(self, request, *args, **kwargs):
        # username = request.user_display_user
        initial_data = {
                'subject': 'MATH',
                'grade' : '5',
        }

        context = {"upload_file_form": UploadFileModelForm(initial=initial_data)}
        return render(request, self.template_name, context=context)


class SuccessView(TemplateView):
    template_name = "pages/upload_success.html"
