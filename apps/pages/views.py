from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from revproxy.views import ProxyView


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutView(TemplateView):
    template_name = "pages/about.html"


class FileInformationView(TemplateView):
    template_name = "pages/fileinformation.html"


class WhyUseView(TemplateView):
    template_name = "pages/whyuse.html"


class ResultsExplainedView(TemplateView):
    template_name = "pages/results_explained.html"


FILE_MANAGER_URL = "http://54.160.87.107:5000/doc"


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class TestProxyView(ProxyView, LoginRequiredMixin):
    upstream = FILE_MANAGER_URL

