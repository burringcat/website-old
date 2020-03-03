"""
Django settings for wvr project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import json
import os
from django.utils.translation import ugettext_lazy as _
from django import http

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('WVR_SECRET_KEY', 'u*uuv-4lta=2ous$%dm!h38k#e&xaoga!*ep(mb4@(t!c2am49')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('WVR_DEBUG') is not None
if DEBUG is True:
    print("Warning: DEBUG is on.")
ALLOWED_HOSTS = ['your-host-for.website']
if DEBUG is True:
    ALLOWED_HOSTS += ['*']
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'weblog',
    'utils',
    'landing_page',
    'wvr_auth',
    'site_info',
    'about_me',
    'shortener',
    'f1l3',
]

MIDDLEWARE = [
    'utils.middleware.IPMiddleware',
    'utils.middleware.CountryMiddleware',
    'utils.middleware.CountryRedirectMiddleware',
    'site_info.middleware.StatisticsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wvr.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'utils.context_processors.settings',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wvr.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
LANDING_PAGE_AUDIO_URL = 'https://misc.0u0.fun/audios/diamond_city.webm'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles"),
]
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'
HAN_CHARACTER_SLUG_STYLE = 'Pinyin'  # Roman, Pinyin or as-is
BLOG_AUTO_TRANSLATE = False
WEBLOG_URL = ''  # or None. if specified, the blog view will redirect to there
ADMIN_URL = os.environ.get('WVR_ADMIN_URL', 'admin')
PRIMARY_HOST_URL = 'https://your-host-for.website' if not DEBUG \
    else 'http://localhost'
LANGUAGES = (
    ('en', _('English')),
)
LANGUAGES_DICT = dict(LANGUAGES)
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
LANGUAGE_COOKIE_NAME = 'override_language_code'
yn = ("yes", "no")
trans_yn = (_("yes"), _("no"))
SITE_CONFIG = (
    (LANGUAGE_COOKIE_NAME, LANGUAGES_DICT.keys(), LANGUAGES_DICT.keys()),
    ('use_translation', yn, trans_yn),
    ('country_redirect', yn, trans_yn),
)
BLOG_POST_EDITOR_WIDGET = 'utils/widgets/text_input_with_blob_image.html'
UTILS_BACKGROUND_PATH = os.path.join(BASE_DIR, 'utils/background_images/')
UTILS_PUBLIC_UTILS = (
    #  url names/view names
    'ping',
    'shortener',
)
UTILS_COUNTRY_REDIRECT = (

)
GEOIP_PATH = os.path.join(BASE_DIR, 'utils/utils/geoip_database')


if DEBUG is False:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'mail.gandi.net'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = os.environ.get('WVR_EMAIL_HOST_USER') or ''
    EMAIL_HOST_PASSWORD = os.environ.get('WVR_EMAIL_HOST_USER') or ''
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
else:
    DEFAULT_FROM_EMAIL = 'google@google.com'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ABOUT_ME_CV_PATHS = (
    ('en', os.path.join(BASE_DIR, 'about_me/templates/about_me/cv.md')),
)
ABOUT_ME_CV_PATHS_DICT = dict(ABOUT_ME_CV_PATHS)
ABOUT_ME_MARKDOWN = os.path.join(BASE_DIR, 'about_me/templates/about_me/empty.md')
ABOUT_ME_AUDIO_URL = 'https://misc.0u0.fun/audios/cs_italy.m4a'


SITE_INFO_CLEAR_OLD_VISITOR_DATA = True


LOGIN_URL = '/auth/login/'
WVR_AUTH_GITHUB_ID = os.environ.get('WVR_AUTH_GITHUB_ID')
WVR_AUTH_GITHUB_SECRET = os.environ.get('WVR_AUTH_GITHUB_SECRET')

WEBCHAT_DEFAULT_ROOM = 'random'

SHORTENER_URL_ENCRYPT_PREFIX = 'encrypted-'


F1L3_MAX_FILE_SIZE_MB = 64

# Not implemented
# F1L3_MAX_FILE_AGE_DAYS = 15
# F1L3_ENABLE_ADMIN_FEATURES = True

F1L3_ROOT = os.path.join(MEDIA_ROOT, 'f1l3')
F1L3_URL = os.path.join(MEDIA_URL, 'f1l3/')


SITE_TITLE = 'OvO'

TOPBAR_F1L3 = True
# TOPBAR_GIT_SITE: set to empty or None to disable this button
TOPBAR_GIT_SITE = 'https://github.com/burringcat'


try:
    from wvr.local_settings.local import *
except ImportError:
    pass