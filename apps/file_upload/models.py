import uuid

from django.contrib.auth.models import User
from django.db import models


class FileInfo(models.Model):
    """
    A file information object created for each trained file uploaded to the S3 bucket.

    Important Fields
    owner - links the user account to their uploaded file
    file_id - unique ID assigned to uploaded file used to later retrieve the file_path.
    This value is shown in the GET HTTP request. It is designed to be random enough to where
    it cannot be guessed by a user who is not the owner.
    file_path - the path to the file inside the S3 bucket, in the format 'uploads/.../...csv'
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="file_owner")

    creation_date = models.DateTimeField(auto_now_add=True)

    file_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    file_name = models.TextField()
    file_path = models.TextField()

    grade = models.CharField(max_length=2)
    subject = models.CharField(max_length=25)
