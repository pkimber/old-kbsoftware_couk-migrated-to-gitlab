# -*- encoding: utf-8 -*-
from .local import *

DATABASE = 'dev_www_kbsoftware_co_uk_malcolm'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE,
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


INSTALLED_APPS += (
    'debug_toolbar',
)

OPBEAT['APP_ID'] = None
