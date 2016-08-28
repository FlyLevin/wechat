"""
Django settings for yimi project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l#-+krn7o=*6g&ien3$c^p2(*+tp*-hibs2zhygwy72j3+dt_1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = '*'

TOKEN = 'flylevin'

SAE_STORAGE_DOMAIN = 'jiedianstorage'

SAE_APPNAME = 'flylevin'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'south',
    'apps.nanjing',
    'myueditor',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'yimi.urls'

WSGI_APPLICATION = 'yimi.wsgi.application'

# Define the session settings
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

import os.path
from os import environ
debug = not environ.get("APP_NAME", "")
if debug:
    MYSQL_DB = 'app_saepy'
    MYSQL_USER = 'root'
    MYSQL_PASS = '********'
    MYSQL_HOST_M = '127.0.0.1'
    MYSQL_HOST_S = '127.0,0,1'
    MYSQL_PORT = '3306'
else:
    import sae.const
    MYSQL_DB = sae.const.MYSQL_DB
    MYSQL_USER = sae.const.MYSQL_USER
    MYSQL_PASS = sae.const.MYSQL_PASS
    MYSQL_HOST_M = sae.const.MYSQL_HOST
    MYSQL_HOST_S = sae.const.MYSQL_HOST_S
    MYSQL_PORT = sae.const.MYSQL_PORT


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': MYSQL_DB,
        'USER': MYSQL_USER,
        'PASSWORD': MYSQL_PASS,
        'HOST': MYSQL_HOST_M,
        'PORT': MYSQL_PORT,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'static'),
   # '/usr/local/lib/python2.7/site-packages/django/contrib/admin/static',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'templates'),
)

MEDIA_ROOT = '*'
MEDIA_URL = '/media/'

TOKEN_CACHE_PRE = 'yimi_access_token'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

#GROUP_API = { 
#    'create_group': 'https://api.weixin.qq.com/cgi-bin/groups/create?access_token=',
#    'get_all_group': 'https://api.weixin.qq.com/cgi-bin/groups/get?access_token=',
#    'select_user_group': 'https://api.weixin.qq.com/cgi-bin/groups/getid?access_token=',
#    'update_group': 'https://api.weixin.qq.com/cgi-bin/groups/update?access_token=',
#    'change_user_group': 'https://api.weixin.qq.com/cgi-bin/groups/members/update?access_token=',
#}

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.i18n",
    "django.core.context_processors.csrf",
)
