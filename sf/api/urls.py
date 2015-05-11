#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^new/$', views.new, name='new'),
    url(r'^show_list/$', views.show_list, name='show_list'),
)
