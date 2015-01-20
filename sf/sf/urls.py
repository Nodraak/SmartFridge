#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^is_in_fridge/$', views.is_in_fridge, name='is_in_fridge'),
    url(r'^get/$', views.get, name='get'),
    url(r'^new/$', views.new, name='new'),
    url(r'^find_recipe/$', views.find_recipe, name='find_recipe'),
)
