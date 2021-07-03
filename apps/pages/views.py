from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutView(TemplateView):
    template_name = "pages/about.html"
