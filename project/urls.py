# -*- encoding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework.authtoken import views


admin.autodiscover()


urlpatterns = [
    url(regex=r'^',
        view=include('login.urls')
        ),
    url(regex=r'^admin/',
        view=include(admin.site.urls)
        ),
    url(regex=r'^api/0.1/',
        view=include('crm.urls_api')
        ),
    url(regex=r'^block/',
        view=include('block.urls.block')
        ),
    url(regex=r'^compose/',
        view=include('compose.urls.compose')
        ),
    url(regex=r'^contact/',
        view=include('contact.urls')
        ),
    url(regex=r'^crm/',
        view=include('crm.urls')
        ),
    url(regex=r'^dash/',
        view=include('dash.urls')
        ),
    url(regex=r'^invoice/',
        view=include('invoice.urls')
        ),
    url(regex=r'^mail/',
        view=include('mail.urls')
        ),
    url(regex=r'^search/',
        view=include('search.urls')
        ),
    url(regex=r'^stock/',
        view=include('stock.urls')
        ),
    url(regex=r'^token/$',
        view=views.obtain_auth_token,
        name='api.token.auth',
        ),
    url(regex=r'^wizard/',
        view=include('block.urls.wizard')
        ),
    # this url include should come last
    url(regex=r'^',
        view=include('block.urls.cms')
        ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#   ^ helper function to return a URL pattern for serving files in debug mode.
# https://docs.djangoproject.com/en/1.5/howto/static-files/#serving-files-uploaded-by-a-user

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
