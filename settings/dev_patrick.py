# -*- encoding: utf-8 -*-
from .local import *

DATABASE = 'test_www_kbsoftware_co_uk_patrick'

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

# Celery
from kombu import Exchange, Queue
# transport
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
# number of worker processes (will be 3 == controller, worker and beat)
CELERYD_CONCURRENCY = 1
# rate limits
CELERY_DISABLE_RATE_LIMITS = True
# serializer
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
# queue
CELERY_DEFAULT_QUEUE = DATABASE
CELERY_QUEUES = (
    Queue(DATABASE, Exchange(DATABASE), routing_key=DATABASE),
)

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'temp.db',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': '',
#         'PORT': '',
#     }
# }

# Django debug toolbar
# INSTALLED_APPS += (
#     'debug_toolbar',
# )
# INTERNAL_IPS = ('127.0.0.1',)
# DEBUG_TOOLBAR_CONFIG = {
#     'INTERCEPT_REDIRECTS': False,
#     'ENABLE_STACKTRACES': True,
# }
OPBEAT['APP_ID'] = None
