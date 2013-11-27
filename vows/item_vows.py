#!/usr/bin/env python
# -*- coding: utf-8 -*-

# correios-frete
# https://github.com/adonescunha/correios-frete

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Adones Cunha adonescunha@gmail.com


from pyvows import Vows, expect
from random import randint

from correios_frete import Item


@Vows.batch
class ItemVows(Vows.Context):

    class WhenInitialized(Vows.Context):

        class WithoutParameters(Vows.Context):

            def topic(self):
                attributes = ('weight', 'height', 'width', 'length')

                for attribute in attributes:
                    yield (attribute, Item())

            def it_defaults_to_zero(self, topic):
                attribute, item = topic
                expect(getattr(item, attribute)).to_equal(0.0)

        class WithParameters(Vows.Context):

            def topic(self):
                value = randint(1, 10)
                cases = (
                    ('weight', value),
                    ('height', value),
                    ('width', value),
                    ('length', value)
                )

                for attribute, value in cases:
                    yield (attribute, value, Item(**{attribute: value}))

            def it_assigns_provided_value(self, topic):
                attribute, value, item = topic
                expect(getattr(item, attribute)).to_equal(value)

    class WhenAdded(Vows.Context):

        def topic(self):
            item1 = Item(weight=1, height=2, width=3, length=4)
            item2 = Item(weight=4, height=3, width =2, length=5)

            return (item1, item2, item1 + item2)

        def it_has_the_sum_of_weights(self, topic):
            item1, item2, sum_item = topic
            expect(sum_item.weight).to_equal(5)

        def it_has_the_sum_of_heights(self, topic):
            item1, item2, sum_item = topic
            expect(sum_item.height).to_equal(5)

        def it_has_max_width(self, topic):
            item1, item2, sum_item = topic
            expect(sum_item.width).to_equal(3)

        def it_has_max_length(self, topic):
            item1, item2, sum_item = topic
            expect(sum_item.length).to_equal(5)
