"""
Django settings for Scoopy project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ja%y5&^(8q81w+g&sj19q-^%k&23j#sbf0495l&b81**ce%h4='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['jiten08.pythonanywhere.com']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',        # Django's admin interface
    'django.contrib.auth',         # Django's authentication system
    'django.contrib.contenttypes', # Django's content types framework
    'django.contrib.sessions',     # Django's session framework
    'django.contrib.messages',     # Django's messages framework
    'django.contrib.staticfiles',  # Django's static files handling
    'Scoopyapp'                    # Your custom application
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

ROOT_URLCONF = 'Scoopy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Specifies the backend to use for 
                                                                        # rendering templates
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Path to the directory containing the templates
        'APP_DIRS': True,  # Whether or not to look for templates in each app's 'templates' directory
        'OPTIONS': {
            'context_processors': [  # Context processors that add extra context to the templates
                'django.template.context_processors.debug',  # Adds debugging information to the context
                'django.template.context_processors.request',  # Adds request information to the context
                'django.contrib.auth.context_processors.auth',  # Adds user authentication information to the context
                'django.contrib.messages.context_processors.messages',  # Adds message information to the context
            ],
        },
    },
]

WSGI_APPLICATION = 'Scoopy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'  # URL for serving static files

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Default primary key field type for models

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Directory where static files 
                                                    # will be collected for production

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'Static'),  # Additional directories where Django will look for static files
]
