from os import path
from django.utils.translation import ugettext_lazy as _
import environ
from corsheaders.defaults import default_headers

root = environ.Path(__file__) - 4
env = environ.Env(DEBUG=(bool, False), )
environ.Env.read_env(env_file=root('.env'))
BASE_DIR = root()
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', [])

SECRET_KEY = env('SECRET_KEY')

SITE_ID = env('SITE_ID')

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'debug_toolbar',
    'registration',
    'rest_framework',
    'corsheaders',

    'heat_control',
    'auth_ex',
    'schedule',
)

AUTH_USER_MODEL = 'auth_ex.User'
LOGIN_REDIRECT_URL = '/admin/'

# --- STATIC FILES ---
STATIC_URL = '/static/'
STATIC_ROOT = env('STATIC_ROOT', default=(root - 1)('static'))
STATICFILES_DIRS = [
    root('static')
]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# --- MEDIA ---
MEDIA_URL = '/media/'
MEDIA_ROOT = env('MEDIA_ROOT', default=(root - 1)('media'))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': (
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
            )
        }
    },
]

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
)

ROOT_URLCONF = 'heat_control.urls'
WSGI_APPLICATION = 'heat_control.wsgi.application'

USE_TZ = True
TIME_ZONE = 'Europe/Warsaw'

# --- LANGUAGES ---
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en-us'
# LANGUAGES = (
#     ('en', _('English')),
#     ('pl', _('Polish')),
# )
# LOCALE_PATHS = (
#     path.join(BASE_DIR, 'locale'),
# )

# --- FILE UPLOAD ---
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440  # i.e. 2.5 MB
FILE_UPLOAD_PERMISSIONS = None
FILE_UPLOAD_DIRECTORY_PERMISSIONS = None

# --- DATABASE ---
# --- POSTGRESQL
DATABASES = {
    'default': env.db(
        default='postgres://postgres:postgres@postgres:5432/postgres'),
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# --- DJANGO COMPRESSOR ---
# STATICFILES_FINDERS += ('compressor.finders.CompressorFinder',)

# --- CACHE ---
# {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'TIMEOUT': 300,
#     }
# }

# --- DJANGO REGISTRATION REDUX ---
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = False

DEBUG_TOOLBAR_PATCH_SETTINGS = False
INTERNAL_IPS = ['127.0.0.1']

# --- SENTRY ---
# INSTALLED_APPS += ('raven.contrib.django.raven_compat',)
# RAVEN_CONFIG = {
#     'dsn': '',
# }
# LOGGING['handlers']['sentry'] = {
#     'class': 'raven.handlers.logging.SentryHandler',
#     'level': 'WARNING',
# }
# LOGGING['loggers'][''] = {
#     'handlers': ['console', 'sentry'],
#     'level': 'DEBUG',
#     'propagate': False,
# }
# LOGGING['loggers']['heat_control'] = {
#     'handlers': ['sentry'],
#     'level': 'INFO',
#     'propagate': True,
#     'formatter': 'simple',
# }

BASE_MULTICASE_HTTP_HEADER = 'json-key-case'

CORS_ALLOW_HEADERS = default_headers + (
    BASE_MULTICASE_HTTP_HEADER,
)
CORS_ORIGIN_WHITELIST = ()

MULTICASE_HTTP_HEADER = 'HTTP_{}'.format(
    BASE_MULTICASE_HTTP_HEADER.upper().replace('-', '_')
)
CORS_ORIGIN_ALLOW_ALL = True