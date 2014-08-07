# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import (
    patterns,
    url,
)
from django.contrib import admin

from .views import HomeView


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(regex=r'^$',
        view=HomeView.as_view(),
        name='project.home'
        ),
)
