#!/usr/bin/env python
# -*- coding: utf-8 -*-

# correios-frete
# https://github.com/adonescunha/correios-frete

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Adones Cunha adonescunha@gmail.com


from pyvows import Vows, expect

from correios_frete import Package, Item
from correios_frete.constants import CAIXA_PACOTE, ROLO_PRISMA


@Vows.batch
class PackageVows(Vows.Context):

     class WhenInitialized(Vows.Context):

          def topic(self):
               return Package()

          def its_items_list_is_initialized_empty(self, topic):
               expect(len(topic.items)).to_equal(0)

          class ItsReducedItem(Vows.Context):

               def topic(self, topic):
                    attributes = ('weight', 'height', 'width', 'length')

                    for attribute in attributes:
                         yield (topic.reduced_item, attribute)

               def is_initialized_with_default_attribute_values(self, topic):
                    item, attribute = topic
                    expect(getattr(item, attribute)).to_equal(0.0)

          class WithoutParameters(Vows.Context):

               def its_formato_defaults_to_CAIXA_PACOTE(self, topic):
                    expect(topic.formato).to_equal(CAIXA_PACOTE)

          class WithParameters(Vows.Context):

               def topic(self):
                    return Package(formato=ROLO_PRISMA)

               def its_formato_is_assigned(self, topic):
                    expect(topic.formato).to_equal(ROLO_PRISMA)

     class AddItem(Vows.Context):

          def topic(self):
               package = Package()
               args = (
                    ('weight', 1),
                    ('height', 2),
                    ('width', 3),
                    ('length', 4)
               )
               return (args, package.add_item(**dict(args)), package)

          def appends_an_item_to_items_list(self, topic):
               _, item, package = topic
               expect(package.items[-1]).to_equal(item)

          class ReturnsAnItem(Vows.Context):

               def topic(self, topic):
                    args, item, package = topic

                    for attribute, value in args:
                         yield (attribute, value, item, package)

               def with_provided_attributes(self, topic):
                    attribute, value, item, _ = topic
                    expect(getattr(item, attribute)).to_equal(value)

          class ItsReducedItem(Vows.Context):

               def topic(self, topic):
                    args, _, package = topic

                    for attribute, value in args:
                         yield (attribute, value, package.reduced_item)

               def is_updated(self, topic):
                    attribute, value, item = topic
                    expect(getattr(item, attribute)).to_equal(value)

     class Delegates(Vows.Context):

          def topic(self):
               package = Package()
               args = (
                    ('weight', 1),
                    ('height', 2),
                    ('width', 3),
                    ('length', 4)
               )
               package.reduced_item = Item(**dict(args))

               for attribute, value in args:
                    yield (package, attribute, value)

          def reduced_item_properties(self, topic):
               package, attribute, value = topic
               expect(getattr(package, attribute)).to_equal(value)


