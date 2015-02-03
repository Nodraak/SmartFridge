#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.new, name='new'),
    url(r'^get/$', views.get, name='get'),
    url(r'^show_list/$', views.show_list, name='show_list'),
    url(r'^find_product/$', views.find_product, name='find_product'),
    url(r'^find_recipe/$', views.find_recipe, name='find_recipe'),
    url(r'^debug/$', views.debug, name='debug'),
)
