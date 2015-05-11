#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns(
    '',
    url(r'^a/', include(admin.site.urls)),
    url(r'^sf/', include('sf.sf.urls', namespace='sf')),
)
