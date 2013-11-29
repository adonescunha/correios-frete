#!/usr/bin/env python
# -*- coding: utf-8 -*-

# correios-frete
# https://github.com/adonescunha/correios-frete

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Adones Cunha adonescunha@gmail.com


from pyvows import Vows, expect

from correios_frete.utils import comma_separated_to_float, s_n_to_bool


@Vows.batch
class CommaSeparatedToFloatVows(Vows.Context):

    def topic(self):
        return comma_separated_to_float('32,90')

    def it_converts_to_float(self, topic):
        expect(topic).to_equal(32.9)


@Vows.batch
class SNToBoolVows(Vows.Context):

    def topic(self):
        cases = (
            ('S', True),
            ('N', False),
            (None, None)
        )

        for value, expected in cases:
            yield (expected, s_n_to_bool(value))

    def it_converts_to_bool(self, topic):
        expected, actual = topic
        expect(actual).to_equal(expected)
