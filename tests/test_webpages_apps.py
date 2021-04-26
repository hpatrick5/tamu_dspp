from django.apps import apps
from django.test import TestCase

from webpages.apps import WebpagesConfig


class WebpagesConfigTest(TestCase):
    def test_webpages_config_settings(self):
        self.assertEqual(WebpagesConfig.name, 'webpages')
        self.assertEqual(apps.get_app_config('webpages').name, 'webpages')
