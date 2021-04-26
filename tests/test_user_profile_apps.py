from django.apps import apps
from django.test import TestCase

from user_profile.apps import UserProfileConfig


class UserProfileConfigTest(TestCase):
    def test_userprofile_config_settings(self):
        self.assertEqual(UserProfileConfig.name, 'user_profile')
        self.assertEqual(apps.get_app_config('user_profile').name, 'user_profile')
