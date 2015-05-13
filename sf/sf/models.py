#!/usr/bin/env python
# -*- coding: utf-8 -*-


import serial
import struct
from django.db import models


class Position(models.Model):

    x = models.PositiveSmallIntegerField()
    y = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return 'x=%d y=%d' % ((self.x, self.y))


class Product(models.Model):

    name = models.CharField(max_length=128)
    expire = models.DateField()
    nb = models.PositiveSmallIntegerField(default=1)
    calorie = models.PositiveSmallIntegerField()
    position = models.ForeignKey(Position)

    def __unicode__(self):
        return self.name


class ArduiSerialError(Exception):
    pass


class MoveError(ArduiSerialError):
    pass


class SensorError(ArduiSerialError):
    pass


class ResponseError(ArduiSerialError):
    pass


class TryAgainError(ArduiSerialError):
    pass


SFP8_MASK_ORDER = 0b11000000
SFP8_MASK_DATA = 0b00111111

SFP8_ORDER_GOTO = 0b00000000
SFP8_ORDER_PUSH = 0b01000000
SFP8_ORDER_COOLING = 0b10000000
SFP8_ORDER_SENSOR = 0b11000000

SFP8_TRUE = 0b00000001
SFP8_FALSE = 0b00000000
SFP8_SUCCESS = 0b11111111
SFP8_INVALID = 0b00000000


class ArduiSerial(object):

    def __init__(self, port='/dev/ttyACM0', bauds=9600, timeout=1):
        self.STATUS_SUCCESS = SFP8_SUCCESS
        self.STATUS_INVALID = SFP8_INVALID
        self.STATUS_FALSE = SFP8_FALSE
        self.STATUS_TRUE = SFP8_TRUE
        self.STATUS_UNKNOWN = 42

        self.ser = serial.Serial(port, bauds, timeout=timeout)
        self.ser.read()

    #def __del__(self):
    #    self.ser.close()

    def _order_send(self, order):
        order = str(order)
        self.ser.write(order)
        raw = self.ser.read()

        try:
            ret = struct.unpack('!i', '\00\00\00'+raw)[0]
        except:
            raise TryAgainError('Try again')

        if ret == SFP8_SUCCESS:  # success
            return self.STATUS_SUCCESS
        elif ret == SFP8_INVALID:  # invalid request
            raise ResponseError('Invalid request')
            return self.STATUS_INVALID
        elif ret == SFP8_FALSE:  # false / off
            return self.STATUS_FALSE
        elif ret == SFP8_TRUE:  # true / on
            return self.STATUS_TRUE
        else:
            return self.STATUS_UNKNOWN

    def order_floor_go(self, i):
        i = int(i)
        if i not in range(0, 5):
            raise MoveError('Parameters not in bounds')
        else:
            order = SFP8_ORDER_GOTO | int(i)
            return self._order_send(order)

    def order_floor_push(self, i):
        i = int(i)
        if i not in range(0, 5):
            raise MoveError('Parameters not in bounds')
        else:
            order = SFP8_ORDER_PUSH | int(i)
            return self._order_send(order)

    def order_cooling(self, value):
        value = bool(value)
        order = SFP8_ORDER_COOLING | value
        return self._order_send(order)

    def get_product(self, product):
        floor = 2  # product.position not implemented
        self.order_floor_go(floor)
        self.order_floor_push(floor)
