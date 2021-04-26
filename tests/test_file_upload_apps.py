from django.apps import apps
from django.test import TestCase

from file_upload.apps import FileUploadConfig


class FileUploadConfigTestCase(TestCase):
    def test_file_upload_config_settings(self):
        self.assertEqual(FileUploadConfig.name, 'file_upload')
        self.assertEqual(apps.get_app_config('file_upload').name, 'file_upload')
