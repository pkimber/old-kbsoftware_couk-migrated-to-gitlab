# -*- encoding: utf-8 -*-
from django.conf.urls import url

from .views import ContactDetailView, DashView, SettingsView


urlpatterns = [
    url(regex=r'^contact/(?P<pk>\d+)/$',
        view=ContactDetailView.as_view(),
        name='contact.detail'
        ),
    url(regex=r'^$',
        view=DashView.as_view(),
        name='project.dash'
        ),
    url(regex=r'^settings/$',
        view=SettingsView.as_view(),
        name='project.settings'
        ),
]
