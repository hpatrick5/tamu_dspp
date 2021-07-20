from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

from apps.file_upload.models import File_Info


class UserProfileView(TemplateView, LoginRequiredMixin):
    template_name = "account/profile.html"


class UserFileView(TemplateView, LoginRequiredMixin):
    template_name = "account/user_files.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['files'] = File_Info.objects.filter(owner=self.request.user)
        context['files'] = context['files'].order_by('-id')
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.get_context_data())