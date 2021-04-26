"""
Django settings for dspp project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
#legacy code line below
#from pathlib import Path
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#legacy code below
#BASE_DIR = Path(__file__).resolve().parent.parent

#legacy code line below
#from pathlib import Path
#AUTH_USER_MODEL = 'auth.User'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0x9%f5$w(79=-9k*=g_90!)p(rvo4wh)tn)0vrozsscbh5lj2b'
#legacy code below
#SECRET_KEY = '_uv_lnq5n9#)v9-!&2l-@f2%#c@wonam+-b3iprv)_@91b9-h4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['dspp.herokuapp.com']
#ALLOWED_HOSTS = [
 #   'sp21-606-school-district-data.herokuapp.com',
 #   '528da989e1984836ae2c19f615abaf67.vfs.cloud9.us-east-2.amazonaws.com',
 #   'd8ec943f80644b70b7506e130747dc62.vfs.cloud9.us-east-2.amazonaws.com',
 #   '127.0.0.1',
 #   'test-sp21-606-school-district.herokuapp.com',
 #   '2b44a7e254184d5b99660ff4bb8973cf.vfs.cloud9.us-east-2.amazonaws.com',
 #   'c00793065e5e4d24844a82d4aaa3970d.vfs.cloud9.us-east-2.amazonaws.com',
 #   ]
#Mehdi's code below
ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'user_registration',
    'bootstrap4',
    'django_thumbs',
    'anymail',
    'allauth',
    'allauth.account',
    'user_profile',
    'webpages',
    'file_upload'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dspp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dspp.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

#legacy code below
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
##

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 'data' is my media folder

DATE_FORMAT = 'b d, Y'
SHORT_DATE_FORMAT = 'b d, Y'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)
ACCOUNT_AUTHENTICATION_METHOD = "email"
SITE_ID = 1

# TODO - use this for a valid email backend (production/staging only)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # use this in dev
# EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"

EMAIL_SUBJECT_PREFIX = '[Test mail]'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_LOGOUT_ON_GET = True

ANYMAIL = {
    "SENDGRID_API_KEY": os.environ.get('SENDGRID_API_KEY'),
}

import mimetypes
mimetypes.add_type("text/css", ".css", True)

#legacy code below
#STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#RISPY_TEMPLATE_PACK = 'bootstrap4'
#OGIN_REDIRECT_URL = 'login-home'
#LOGIN_URL = 'main-login'
#TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
##end legacy code