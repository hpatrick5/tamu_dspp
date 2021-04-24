from user_profile.models import UserProfile
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class UserProfileModelTestCase(TestCase):
    def setUp(self):
        self.username = 'tuser123'
        self.password = 'PWTest123!'
        self.first_name = 'Test'
        self.last_name = 'User'
        
        
        self.user = User.objects.create_user(self.username, 'email@test.com', self.password)
        
        self.data = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'image': 'Test Image',
            'bio' : 'Test Bio',
            'location': 'Test Location',
        }
        
        self.user.save()
    
    def test_userprofile_object_created_on_user_save(self):
        self.assertEqual(UserProfile.objects.count(), 1)
    
