from django.contrib import admin
from django.contrib.auth.models import Group

from user_profile.models import UserProfile

# Register your models here.
admin.site.unregister(Group)
admin.site.register(UserProfile)
