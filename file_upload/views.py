from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

from file_upload.forms import UploadFileModelForm

#used to downlaod files
import os
from django.conf import settings
from django.http import HttpResponse, Http404

from .models import File
from user_profile.models import UserProfile
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

        if upload_file_form.is_valid():
            temp = upload_file_form.save(commit=False)
            temp.grade = request.POST["grade"]
            temp.upload_file = request.FILES["upload_file"]
            temp.owner = request.user
            temp.save()


            #do we need to have a special save command for foreign key relationships? Im not sure our DB model is
            #working correctly. I ended up finding a work around to only show one file from user upload
            #response.user.file.add(temp)  # adds the to do list to the current logged in user

            #the line below queries the database and pulls all objects from the File table.
            file_path = File.objects.get(upload_file = temp.upload_file)

            import pickle
            import pandas as pd
            import os

            here = os.path.dirname(os.path.abspath(__file__))
            filename = os.path.join(here, 'dummy_ml_model_clf.sav')
            model = pickle.load(open(filename, "rb"))
            df = pd.read_csv(str(file_path))
            X = df.iloc[:, 1:12]
            prediction = model.predict(X)
            pd.DataFrame(prediction).to_csv(filename)

            return render(request, 'file_upload/success.html', {'file_path':file_path})

        messages.error(request, upload_file_form.errors)
        return render(request, self.template_name, context=context)

    # get will be when form is empty, just going to that page
    def get(self, request, *args, **kwargs):
        # context = super(UploadFileView(), self).get_context_data(**kwargs)

        username = request.user.user_profile
        initial_data = {
                'grade' : 0,
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
