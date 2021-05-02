import os

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from file_upload.models import File


class FileModelTestCase(TestCase):
    def setUp(self):
        self.url = reverse("upload")
        self.client = Client()

        self.username = 'tuser123'
        self.password = 'PWTest123!'

        self.user = User.objects.create_user(
            self.username, 'email@test.com', self.password)
        self.client.login(username=self.username, password=self.password)
        self.assertEqual(self.client.get(self.url).status_code, 200)

        with open('tests/files/TESTING-content.csv') as fp:
            self.client.post(
                self.url,
                {
                    'owner': self.user,
                    'subject': 'READING_SPANISH',
                    'grade': '5',
                    'upload_file': fp
                })

        self.assertEqual(File.objects.count(), 1)
        self.file = File.objects.first()

    def test_file_object_returns_correct_str(self):
        self.assertEqual(str(self.file), str(self.file.upload_file))

    def tearDown(self):
        os.remove('media/' + str(self.file.upload_file))
