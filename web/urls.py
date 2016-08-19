# -*- encoding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin

from .views import HomeView


admin.autodiscover()


urlpatterns = [
    url(regex=r'^$',
        view=HomeView.as_view(),
        name='project.home'
        ),
]
