import os

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from file_upload.models import File


class UploadViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse("upload")
        self.client = Client()

        self.username = 'tuser123'
        self.password = 'PWTest123!'

        self.user = User.objects.create_user(
            self.username, 'email@test.com', self.password)
        self.client.login(username=self.username, password=self.password)
        self.assertEqual(self.client.get(self.url).status_code, 200)

        self.upload_failure_empty_file_message = b'The submitted file is empty.'
        self.upload_success_message = b'Your input data has been evaluated by the ML'

    def test_upload_returns_upload_template_for_get(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed("file_upload/upload.html")

    def test_upload_returns_empty_error_for_invalid_post(self):
        with open('tests/files/TESTING-empty.csv') as fp:
            response = self.client.post(
                self.url,
                {
                    'owner': self.user,
                    'subject': 'MATH',
                    'grade': 5,
                    'upload_file': fp

                })
        self.assertTrue(
            self.upload_failure_empty_file_message in response.content)
        self.assertTrue(
            self.upload_success_message not in response.content)

    def test_upload_returns_success_for_valid_post(self):
        with open('tests/files/TESTING-content.csv') as fp:
            response = self.client.post(
                self.url,
                {
                    'owner': self.user,
                    'subject': 'MATH',
                    'grade': 5,
                    'upload_file': fp
                })
        self.assertTemplateUsed("file_upload/success.html")
        self.assertTrue(
            self.upload_success_message in response.content)
        self.assertTrue(
            self.upload_failure_empty_file_message not in response.content)

        # clean-up created files
        os.remove('media/' + str(File.objects.first().upload_file))

    def test_upload_creates_file_object_for_valid_post(self):
        with open('tests/files/TESTING-content.csv') as fp:
            self.client.post(
                self.url,
                {
                    'owner': self.user,
                    'subject': 'MATH',
                    'grade': 5,
                    'upload_file': fp
                })
        self.assertEqual(File.objects.count(), 1)

        # clean-up created files
        os.remove('media/' + str(File.objects.first().upload_file))


class ErrorViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("error")

    def test_error_returns_error_template_for_get(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed("file_upload/error.html")


class SuccessViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("success")

    def test_success_returns_success_template_for_get(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed("file_upload/success.html")
