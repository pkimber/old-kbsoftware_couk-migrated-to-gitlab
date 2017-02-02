# -*- encoding: utf-8 -*-
from kombu import Exchange, Queue
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


OPBEAT['APP_ID'] = None

MIDDLEWARE_CLASSES += MIDDLEWARE_CLASSES + (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS += (
    # 'django.contrib.formtools',
    'django_extensions',
    'debug_toolbar',
)

#force the debug toolbar to be displayed
def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
}

# Celery
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


from celery.schedules import crontab
CELERYBEAT_SCHEDULE = {
    'process_mail': {
        'task': 'mail.tasks.process_mail',
        'schedule': crontab(),
    },
}

import socket

ALLOWED_HOSTS = [
    '127.0.0.1',
    '127.0.1.1',
    'localhost',
    socket.gethostbyname(socket.gethostname())
]

