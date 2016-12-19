# -*- encoding: utf-8 -*-
from __future__ import absolute_import

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
# PJK 15/11/2016, Why do we set this here?  I don't think we should!
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

from django.conf import settings

app = Celery('project')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


from opbeat.contrib.django.models import client, logger, register_handlers
from opbeat.contrib.celery import register_signal

try:
    register_signal(client)
except Exception as e:
    logger.exception('Failed installing celery hook: %s' % e)
    if 'opbeat.contrib.django' in settings.INSTALLED_APPS:
        register_handlers()
