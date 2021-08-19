from django.contrib.auth.models import User
from django.db import models


class FileInfo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="file_owner")
    file_path = models.TextField()
    file_name = models.TextField()
    grade = models.CharField(max_length=2)
    subject = models.CharField(max_length=25)
    creation_date = models.DateTimeField(auto_now_add=True)
