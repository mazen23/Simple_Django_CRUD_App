"""
Django settings for simpleproject project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ['SECRET_KEY']
SECRET_KEY ="ZI3wcyNebVv9llpabPzQbdqMPh4K0l8bY9Xu865VeTU5eowh2iH+atdiKTsgYpw2EKR5GQkFKsllOapTFBIWVJtNWBxXJeVUCt/Wjotxswqr9fEQzcQhlgz62D/KbW/SptBRGXWu0OqvMIXqCS1tKUSPamezKbAcLI5Tlfu7yMdDo7Xl35y/quQQJC/KUb8Kmdpn+fElfZX43oWWnMotbAIAjlke2wudQpD5yhtSYmgdYS/gyu7J9LfTW+vkc1GBLFaaIP83W5gsWVNjWoC32vNUyLAv+lvCXqpmqsfWQySPW5fNFwj/pPGn1bKXU0wBQqck6j0hY4mDGR1E22fwIXtDWUo0deKsXvVoxbFyMIs84qrjHkH45gOhl3nFuxb5cQ1BUriFBmGqQbXtu0AMM+6uYTBR9Icdx95+nwANZYI10MFkDtCHptEwxi9hFBAcAyS9BG/FewlVWWCXftMNbCLRNGU1eM5tgTt9CoLtJlgmDoAJ+pKmInealwMGvqAeimiElEFY/y1a+XDSZS74pYhW3gOZKEYTa4Km+FxKBsgLt0KIAmRlsS8+dN0XOwDiqvsNSI0wrT/gEGbH9nXbnO6Qd3JxCiqMqGjGaYAzkVGn1v2mMzY0azmrbwfhqPTn/fufB59svShnu0Eoia8QKzIUtu5ZMDWTb9eQ0hrY2dc"
# print(SECRET_KEY)




# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']
# ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'books.apps.BooksConfig'
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

ROOT_URLCONF = 'simpleproject.urls'

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

WSGI_APPLICATION = 'simpleproject.wsgi.application'


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

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
