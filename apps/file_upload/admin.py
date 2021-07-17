from django.contrib import admin
from .models import File_Info

# enables the admin accounts to view user profiles
admin.site.register(File_Info)

# Notes for future use: in order to delete everything and start fresh delete db.sqlite3,
# and migration but leave _init_.py
