#!/usr/bin/env python
# -*- coding: utf-8 -*-

# correios-frete
# https://github.com/adonescunha/correios-frete

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Adones Cunha adonescunha@gmail.com


from .constants import CAIXA_PACOTE
from .item import Item


class Package(object):

    def __init__(self, formato=CAIXA_PACOTE):
        self.formato = formato
        self.items = []

    def add_item(self, **item_args):
        item = Item(**item_args)
        self.items.append(item)

        return item
