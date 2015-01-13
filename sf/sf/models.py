#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class Position(object):

    def __init__(self, *arg, **kwarg):
        self.x = 0
        self.y = 0
        super(Position, self).__init__(*arg, **kwarg)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y


class Product(models.Model):

    def __init__(self, *arg, **kwarg):
        self.position = Position()
        super(Product, self).__init__(*arg, **kwarg)

    name = models.CharField(max_length=128)
    expire = models.DateField()
    nb = models.PositiveSmallIntegerField(default=1)
    calorie = models.PositiveSmallIntegerField()
