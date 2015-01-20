#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sf_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^a/', include(admin.site.urls)),
    url(r'^sf/', include('sf.sf.urls', namespace='sf')),
)
