#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Position, Product


admin.site.register(Position)
admin.site.register(Product)
