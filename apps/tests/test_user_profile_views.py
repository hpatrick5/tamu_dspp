from django.test import TestCase, Client
from django.urls import reverse


class UserStatusViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("status")

    def test_userstatus_returns_userstatus_template_for_get(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed("user_profile/status.html")
