#!/usr/bin/env python
# -*- coding: utf-8 -*-

# correios-frete
# https://github.com/adonescunha/correios-frete

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Adones Cunha adonescunha@gmail.com


class Item(object):

    def __init__(self, weight=0.0, height=0.0, width=0.0, length=0.0):
        self.weight = weight
        self.height = height
        self.width = width
        self.length = length

    def __add__(self, other):
        return Item(
            weight=self.weight + other.weight,
            height=self.height + other.height,
            width=max(self.width, other.width),
            length=max(self.length, other.length)
        )
