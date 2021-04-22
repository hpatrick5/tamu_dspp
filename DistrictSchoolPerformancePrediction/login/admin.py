from django.contrib import admin
from . import models
#notes for future use: in order to delete everything and start fresh delete db.sqlite3, and migration but leave _init_.py

# @admin.register(models.School)
# class SchoolAdmin(admin.ModelAdmin):
#     list_display = ('name', 'phone', 'city', 'zipcode')

@admin.register(models.User_Profile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'gender', 'email', 'phone', 'role', 'grade')
    # pass

@admin.register(models.SavedFile)
class SavedFileAdmin(admin.ModelAdmin):
    list_display = ['upload_file']
    # pass
