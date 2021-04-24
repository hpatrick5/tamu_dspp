from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.shortcuts import redirect, reverse
from user_profile.forms import UserProfileModelForm, UserDetailModelForm
from django.contrib import messages

from file_upload.forms import UploadFileModelForm

from .models import File

# Create your views here.

# accepted file types for upload
ACCEPTED_FILE_TYPES = ['csv']

#uncomment this for login required
class UploadFileView(TemplateView, LoginRequiredMixin):
#class UploadFileView(TemplateView):
    template_name = "file_upload/upload.html"
    
    #username = request.user.user_profile
   

    def post(self, request, *args, **kwargs):
        #context = super(UploadFileView(), self).get_context_data(**kwargs)
        #context['upload_file_form'] = upload_file_form = UploadFileModelForm(request.POST, request.FILES,
        #                                                                       instance=request.user.user_profile)
        
        context = {"upload_file_form": UploadFileModelForm(instance=request.user.user_profile)}
        #context = {"upload_file_form": UploadFileModelForm()}

        upload_file_form = UploadFileModelForm(request.POST, request.FILES)
        
        if upload_file_form.is_valid():
            temp = upload_file_form.save(commit=False)
            
            temp.grade = request.POST["grade"]
            temp.upload_file = request.FILES["upload_file"]
            temp.owner = request.user
            temp.save()
            
            #trying to save foreign key (?)
            
            return render(request, 'file_upload/success.html')
        else:
            messages.error(request, upload_file_form.errors)
        
        return render(request, self.template_name, context=context)
    
    #get will be when form is empty, just going to that page
    def get(self, request, *args, **kwargs):
        #context = super(UploadFileView(), self).get_context_data(**kwargs)
        #context['upload_file_form'] = UploadFileModelForm(instance=request.user.user_profile)
        username=request.user.user_profile
        initial_data = {
                'name' : username,
                'grade' :0}
            
        #legacy code
        #context = {"upload_file_form": UploadFileModelForm(instance=request.user.user_profile)}
        context = {"upload_file_form": UploadFileModelForm(initial=initial_data)
            
        }

        #context['user_detail_form'] = UserDetailModelForm(instance=request.user)
        return render(request, self.template_name, context=context)



#class UploadView(TemplateView):
 #   template_name = "file_upload/upload.html"

class ErrorView(TemplateView):
    template_name = "file_upload/error.html"

class SuccessView(TemplateView):
    template_name = "file_upload/success.html"