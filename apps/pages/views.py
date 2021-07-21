from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutView(TemplateView):
    template_name = "pages/about.html"
    
    
FILE_MANAGER_URL = "http://54.160.87.107:5000/doc"

class UserFilesView(TemplateView, LoginRequiredMixin):
    template_name = "account/user_files.html"
    
    def get(self, request, *args, **kwargs):
        # username = request.user_display_user
        
        return render(request, self.template_name)

