from django.apps import apps
from django.test import TestCase

from user_registration.apps import UserRegistrationBs4Config


class UserRegistrationBs4ConfigTest(TestCase):
    def test_userregistrationbs4_config_settings(self):
        self.assertEqual(UserRegistrationBs4Config.name, 'user_registration')
        self.assertEqual(
            apps.get_app_config('user_registration').name, 'user_registration')
