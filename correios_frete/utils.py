#!/usr/bin/env python
# -*- coding: utf-8 -*-

# correios-frete
# https://github.com/adonescunha/correios-frete

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Adones Cunha adonescunha@gmail.com


def comma_separated_to_float(value):
    return float(value.replace(',', '.'))

def s_n_to_bool(value):
    return {'S': True, 'N': False, None: None}[value]
