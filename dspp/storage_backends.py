from storages.backends.s3boto3 import S3Boto3Storage


# For S3 static file storage
# See https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/ for more information
class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'
