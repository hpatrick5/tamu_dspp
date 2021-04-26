from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "webpages/homepage.html"


class TermsView(TemplateView):
    template_name = "webpages/terms.html"


class AboutView(TemplateView):
    template_name = "webpages/about.html"
