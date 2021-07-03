import allauth

from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class UserProfileView(TemplateView, LoginRequiredMixin):
    template_name = "account/profile.html"
