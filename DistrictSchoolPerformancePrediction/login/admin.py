from django.contrib import admin

# Register your models here.

#added for file upload
from .models import User_Profile

#added for file upload
#enables the admin accounts to view user profiles
admin.site.register(User_Profile)


#notes for future use: in order to delete everything and start fresh delete db.sqlite3, and migration but leave _init_.py