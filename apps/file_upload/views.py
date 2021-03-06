from apps.file_upload.forms import FileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from .models import FileInfo
from .utils import get_trained_file, upload_data_to_bucket


VALID_STAAR_TESTS = ["reading_3", "math_3", "reading_4", "math_4", "writing_4", "reading_5", "math_5", "science_5",
                     "reading_6", "math_6", "reading_7", "math_7", "writing_7", "reading_8", "math_8", "science_8",
                     "socialstudies_8"]


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class UploadFileView(TemplateView, LoginRequiredMixin):
    template_name = "pages/upload.html"

    def post(self, request, *args, **kwargs):
        """
        Submit uploaded information file CSV for prediction and upload to S3 bucket.
        """
        context = {"file_form": FileForm()}
        form = FileForm(request.POST, request.FILES)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            grade = form.cleaned_data['grade']

            # Error checking: only allow valid grade/subject combination to be selected
            subject_grade = subject.lower() + "_" + grade
            if subject_grade not in VALID_STAAR_TESTS:
                messages.warning(request, 'Error: ' + subject + ' STAAR test for Grade ' + grade + " does not exist.")
                return HttpResponseRedirect('upload')

            file = request.FILES['file']

            file_type = file.name.split('.')[-1]
            file_type = file_type.lower()

            # Error checking: only allow CSV files to be uploaded
            if file_type != 'csv':
                messages.warning(request, 'Error: Please upload a CSV file.')
                return HttpResponseRedirect('upload')

            # Error checking: prevent CSV files with incorrect headers from being uploaded
            try:
                trained_file = get_trained_file(file, subject_grade, request.user)
            except KeyError:
                messages.warning(request, 'Error: Please make sure that the headers in your uploaded CSV file match '
                                          'the provided template.')
                return HttpResponseRedirect('upload')

            file_info = FileInfo()

            file_info.owner = request.user
            file_info.file_path = upload_data_to_bucket(trained_file, request.user.username)
            file_info.file_name = trained_file.name
            file_info.grade = grade
            file_info.subject = subject

            file_info.save()

            messages.info(request, "Success! Your input data has been evaluated by the ML model, and the predicted "
                                   "scores are ready. Download them below.")
            return HttpResponseRedirect("accounts/profile/files")

        messages.warning(request, "Error: " + form.errors.get_json_data()["file"][0]["message"])
        return render(request, self.template_name, context=context)

    def get(self, request, *args, **kwargs):
        context = {"file_form": FileForm()}
        return render(request, self.template_name, context=context)
