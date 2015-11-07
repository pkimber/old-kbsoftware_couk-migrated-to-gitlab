# -*- encoding: utf-8 -*-
from django.conf.urls import (
    patterns,
    url,
)

from .views import (
    DashView,
    SettingsView,
)


urlpatterns = patterns(
    '',
    url(regex=r'^$',
        view=DashView.as_view(),
        name='project.dash'
        ),
    url(regex=r'^settings/$',
        view=SettingsView.as_view(),
        name='project.settings'
        ),
)
