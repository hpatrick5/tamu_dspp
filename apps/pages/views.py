from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutView(TemplateView):
    template_name = "pages/about.html"


class FileInformationView(TemplateView):
    template_name = "pages/file_info.html"


class WhyUseView(TemplateView):
    template_name = "pages/why_use.html"


class ResultsExplainedView(TemplateView):
    template_name = "pages/results_explained.html"


