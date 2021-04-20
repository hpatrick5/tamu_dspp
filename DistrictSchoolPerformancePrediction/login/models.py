from django.db import models
from django.contrib.auth.models import User

# class upload_file_model(models.Model):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()
#     auth_user = models.ForeignKey(User, on_delete=models.CASCADE)


#A file object is mainly to associate a file with an object or profile. We will learn more about file object in the upcoming section
#note to self: address user to file identification


###
# added for file upload

#class User(models.Model):
#    user_name = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    #last_name = models.CharField(max_length=30)
    #email = models.EmailField()

#   def __str__(self):
#       return (self.user_name)


    #currently this model only allows one upload per user!
class User_Profile(models.Model):
    #fname = models.CharField(max_length=200)\

    #not a one to one field rather many to one
    fname = models.ForeignKey(User, on_delete=models.CASCADE)

    #grade = models.PositiveIntegerField(max_digits=2,decimal_places=2, default=1)
    grade = models.PositiveIntegerField(default=1)

   # class subject(models.TextChoices):
   #     Math = 'Math', _('Math')
    #    Reading = 'Reading', _('Reading')
#
   # course_subject = models.CharField(
    #    max_length=7,
   #     choices=subject.choices,
    #    default=subject.Null,
    #)

    save_file = models.FileField(upload_to='uploads/%Y/%m/%d/', default=None)

   # username = user.get_username()
    #lname = models.CharField(max_length = 200)
    #technologies = models.CharField(max_length=500)
    #email = models.EmailField(default = None)
    display_picture = models.FileField()



    def __str__(self):
        return self.fname

### end of file upload