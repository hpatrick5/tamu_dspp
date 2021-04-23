from django.contrib import admin
from user_profile.models import UserProfile
from django.contrib.auth.models import Group

# Register your models here.
admin.site.unregister(Group)
admin.site.register(UserProfile)
