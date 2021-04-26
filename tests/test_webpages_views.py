from django.test import TestCase, Client
from django.urls import reverse


class HomeViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("homepage")

    def test_home_returns_home_template_for_get(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed("webpages/homepage.html")


class TermsViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("terms")

    def test_terms_returns_terms_template_for_get(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed("webpages/terms.html")
