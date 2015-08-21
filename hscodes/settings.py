"""
Django settings for hscodes project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ftw!-0wj)9x5*0_7kkk_jdz_2hf)m-4f5g9#)fze_tkzdzihc5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hs_search',
    'ajax_select',
    'tagging',
    'haystack',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr/hscode',
        'TIMEOUT': 60 * 5,
        'INCLUDE_SPELLING': True,
        'BATCH_SIZE': 1000,
        'SILENTLY_FAIL': True,
    },
}

ROOT_URLCONF = 'hscodes.urls'

WSGI_APPLICATION = 'hscodes.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hscode',
        'USER':'root',
        'PASSWORD':'',

    }
}

TEMPLATE_CONTEXT_PROCESSORS =[
    'django.core.context_processors.request',
    'django.template.context_processors.request',
    'django.contrib.auth.context_processors.auth',
]
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'hs_search/templates'),
)

# define the lookup channels in use on the site
AJAX_LOOKUP_CHANNELS = {
    #  simple: search
    # 'hs4': {'model': 'hs_search.itc_hscode', 'search_field': 'hs4'},
    # 'hs_code_hs5': {'model': 'hs_search.itc_hscode', 'search_field': 'hs5'},
    # define a custom lookup channel
    'hs4' : ('hs_search.lookups', 'HS4Lookup'),
    'hs8' : ('hs_search.lookups', 'HS8Lookup')
}

FORCE_LOWERCASE_TAGS = True