from django.apps import apps
from django.test import TestCase

from apps.webpages.apps import WebpagesConfig


class WebpagesConfigTest(TestCase):
    def test_webpages_config_settings(self):
        self.assertEqual(WebpagesConfig.name, 'pages')
        self.assertEqual(apps.get_app_config('pages').name, 'pages')
