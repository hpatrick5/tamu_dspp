from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import RegexValidator

# class School(models.Model):
#     name    = models.CharField(max_length=300, help_text='first name, middle and family name, eg. First Middle Family')
#     phone   = models.CharField(validators=[RegexValidator(regex=r'^\+?1?\d{10,15}$', message="Phone number must starts with +1 and in the format: '+12345678900'. Up to 12 digits allowed.")],\
#         help_text="Phone number must be entered in the format: '+123456789'. Up to 11 digits allowed.",\
#         max_length=17, blank=True)
#     city    = models.CharField(max_length=50, help_text='city name, eg. College Station',blank=True)
#     zipcode = models.CharField(max_length=5, help_text='five digits, eg. 12345', blank=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         ordering = ['name']

class User_Profile(models.Model):
    # school          = models.ForeignKey(School, on_delete=models.CASCADE)
    first_name      = models.CharField(max_length=300, blank=True,)
    last_name       = models.CharField(max_length=300, blank=True,)
    email           = models.CharField(max_length=300, blank=True,)
    phone           = models.CharField(validators=[RegexValidator(regex=r'^\+?1?\d{10,11}$', message="Phone number must be entered in the format: '+123456789'. Up to 11 digits allowed.")], max_length=11, blank=True)
    grade           = models.PositiveIntegerField(default=1)
    # course          = models.CharField(max_length=300)
    # save_file       = models.FileField(upload_to='uploads/%Y/%m/%d/', default=None)
    # upload_file     = models.FileField()
    # upload_file     = models.ManyToManyField('SavedFile', help_text='select *.csv file')

    Name = first_name
    Grade = grade
    GENDER = (
        ('m', 'male'),
        ('f', 'female'),
        ('n', 'not applicable')
    )
    gender  = models.CharField(max_length=1, choices=GENDER, default='n', blank=True)

    RESPONSIBILITY =(
        ('t', 'Teacher'),
        ('m', 'Manager'),
        ('o', 'other')
    )
    role  = models.CharField(max_length=1, choices=RESPONSIBILITY, default='t', blank=True)

    def __str__(self):
        return (self.first_name + self.last_name)

    class Meta:
        ordering = ['last_name']

class SavedFile(models.Model):
    user_profile   = models.ForeignKey(User_Profile, on_delete=models.CASCADE)
    upload_file    = models.FileField()
    # save_file      = models.FileField(upload_to='uploads/%Y/%m/%d/', default=None)
    File = upload_file

    def __str__(self):
        return 'saved file'


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
# class User_Profile(models.Model):
#     fname = models.ForeignKey(User, on_delete=models.CASCADE)
#     grade = models.PositiveIntegerField(default=1)
#     save_file = models.FileField(upload_to='uploads/%Y/%m/%d/', default=None)
#     display_picture = models.FileField()

    #currently this model only allows one upload per user!
# class User_Profile(models.Model):
    #fname = models.CharField(max_length=200)\

    #not a one to one field rather many to one
    # Name = models.ForeignKey(User, on_delete=models.CASCADE)

    #grade = models.PositiveIntegerField(max_digits=2,decimal_places=2, default=1)
    # Grade = models.PositiveIntegerField(default=1)

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