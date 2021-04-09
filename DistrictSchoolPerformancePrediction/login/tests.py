from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY
from django.test import TestCase


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'firsttest',
            'password': 'testing321'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)

    def register_setup(self):
        self.credentials = {
            'username': 'newtest',
            'email': 'test@test.com',
            'password1': '123',
            'password2': '123'
        }
        # User.objects.create_user(**self.credentials)

    def test_register(self):
        response = self.client.post(
            '/register/', self.credentials, follow=True)
        # print(response.context['user'])
        self.login_creds = {
            'username': 'newtest',
            'password': '123'
        }
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)
