from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import RegexValidator

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

class School(models.Model):
    name    = models.CharField(max_length=300, blank=True)
    phone   = models.CharField(validators=[RegexValidator(regex=r'^\+?1?\d{10,11}$', message="Phone number must be entered in the format: '+123456789'. Up to 11 digits allowed.")], max_length=17, blank=True)
    city    = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return self.name


class User_Profile(models.Model):
    school          = models.ForeignKey(School, on_delete=models.CASCADE, blank=True)
    name            = models.CharField(max_length=300, blank=True)
    email           = models.CharField(max_length=300, blank=True)
    phone           = models.CharField(validators=[RegexValidator(regex=r'^\+?1?\d{10,11}$', message="Phone number must be entered in the format: '+123456789'. Up to 11 digits allowed.")], max_length=17, blank=True)
    # course          = models.CharField(max_length=300)
    grade           = models.PositiveIntegerField(default=1)
    # save_file       = models.FileField(upload_to='uploads/%Y/%m/%d/', default=None)
    upload_file     = models.FileField()

    GENDER = (
        ('m', 'male'),
        ('f', 'female'),
        ('n', 'not applicable')
    )
    gender  = models.CharField(max_length=1, choices=GENDER, default='n', blank=True)

    ROLE =(
        ('t', 'Teacher'),
        ('m', 'Manager'),
        ('o', 'other')
    )
    responsibility  = models.CharField(max_length=1, choices=ROLE, default='t', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        pass


# class User_Profile(models.Model):
#     fname = models.ForeignKey(User, on_delete=models.CASCADE)
#     grade = models.PositiveIntegerField(default=1)
#     save_file = models.FileField(upload_to='uploads/%Y/%m/%d/', default=None)
#     display_picture = models.FileField()

    #currently this model only allows one upload per user!
# class User_Profile(models.Model):
    #fname = models.CharField(max_length=200)\

    #not a one to one field rather many to one
    # fname = models.ForeignKey(User, on_delete=models.CASCADE)

    #grade = models.PositiveIntegerField(max_digits=2,decimal_places=2, default=1)
    # grade = models.PositiveIntegerField(default=1)

   # class subject(models.TextChoices):
   #     Math = 'Math', _('Math')
    #    Reading = 'Reading', _('Reading')
#
   # course_subject = models.CharField(
    #    max_length=7,
   #     choices=subject.choices,
    #    default=subject.Null,
    #)

    # save_file = models.FileField(upload_to='uploads/%Y/%m/%d/', default=None)

   # username = user.get_username()
    #lname = models.CharField(max_length = 200)
    #technologies = models.CharField(max_length=500)
    #email = models.EmailField(default = None)
    # display_picture = models.FileField()

### end of file upload