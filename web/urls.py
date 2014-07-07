# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import (
    include,
    patterns,
    url,
)
from django.conf.urls.static import static
from django.contrib import admin

from .views import (
    DashView,
    HomeView,
)


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(regex=r'^$',
        view=HomeView.as_view(),
        name='project.home'
        ),
    url(regex=r'^dash/$',
        view=DashView.as_view(),
        name='project.home.user'
        ),
)
