from apps.file_upload.models import FileInfo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class UserProfileView(TemplateView, LoginRequiredMixin):
    template_name = "account/profile.html"


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class UserFileView(TemplateView, LoginRequiredMixin):
    template_name = "account/user_files.html"

    def get_context_data(self, **kwargs):
        """
        Populate files on User Files page with their associated files.
        """
        context = super().get_context_data(**kwargs)
        context['files'] = FileInfo.objects.filter(owner=self.request.user)
        context['files'] = context['files'].order_by('-id')
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.get_context_data())
