from django.contrib import admin
from .models import File

# enables the admin accounts to view user profiles
admin.site.register(File)

# Notes for future use: in order to delete everything and start fresh delete db.sqlite3,
# and migration but leave _init_.py
