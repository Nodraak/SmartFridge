#!/usr/bin/env python
# -*- coding: utf-8 -*-


import serial

from django.db import models

"""
class Position(object):

    def __init__(self, *arg, **kwarg):
        self.x = 0
        self.y = 0
        #super(Position, self).__init__(*arg, **kwarg)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y
"""

class Product(models.Model):

    def __init__(self, *arg, **kwarg):
        #self.position = Position()
        super(Product, self).__init__(*arg, **kwarg)

    name = models.CharField(max_length=128)
    expire = models.DateField()
    nb = models.PositiveSmallIntegerField(default=1)
    calorie = models.PositiveSmallIntegerField()


class ArduiSerial(object):

    def __init__(self):
        self.STATUS_SUCCESS = 0
        self.STATUS_INVALID = 1
        self.STATUS_FALSE = 2
        self.STATUS_TRUE = 3

        self.ser = serial.Serial('/dev/tty.usbmodem1411', 9600, timeout=1)

    def __del__(self):
        self.ser.close()

    def _order_send(self, order):
        self.ser.write(order)
        ret = self.ser.read()

        if ret == 0b10101010:  # success
            self.STATUS_SUCCESS
        elif ret == 0b11111111:  # invalid request
            self.STATUS_INVALID
        elif ret == 0b00000000:  # false / off
            self.STATUS_FALSE
        elif ret == 0b00000001:  # true / on
            self.STATUS_TRUE

    def order_move(self, x, y):
        x, y = int(x), int(y)
        if x < 0 or x > 7 or y < 0 or y > 7:
            print 'error'
            exit()
        else:
            order = (0b00 << 6) | (x << 3) | y
            self._order_send(order)

    def order_cooling(self, value):
        value = bool(value)
        order = (0b01 << 6) | value
        self._order_send(order)

    def get_cooling(self):
        order = (0b01 << 6) | 0b10
        self._order_send(order)

    def get_sensors(self, id):
        id = int(id)
        if id < 0 or id > 3:
            print 'error'
            exit()
        order = 0b10 | id
        self._order_send(order)

