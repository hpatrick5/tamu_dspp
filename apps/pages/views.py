from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from revproxy.views import ProxyView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutView(TemplateView):
    template_name = "pages/about.html"

class FileInformationView(TemplateView):
    template_name = "pages/fileinformation.html"

    
    
FILE_MANAGER_URL = "http://54.160.87.107:5000/doc"
# Doesn't look like we are using the below view
# @method_decorator(, name='dispatch')
# class UserFilesView(TemplateView, LoginRequiredMixin):
#     template_name = "account/user_files.html"
    
#     # @login_required(login_url='/accounts/login/')
#     def get(self, request, *args, **kwargs):
#         # username = request.user_display_user
#         return render(request, self.template_name)

@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class TestProxyView(ProxyView, LoginRequiredMixin):
    upstream = FILE_MANAGER_URL