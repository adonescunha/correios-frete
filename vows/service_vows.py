#!/usr/bin/env python
# -*- coding: utf-8 -*-

# correios-frete
# https://github.com/adonescunha/correios-frete

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Adones Cunha adonescunha@gmail.com


from pyvows import Vows, expect
from .utils import create_sudsobject_mock

from correios_frete import Service


TEST_CASES = (
    ('codigo', '40010'),
    ('valor', 71.00),
    ('prazo_entrega', 1),
    ('valor_mao_propria', 0.0),
    ('valor_aviso_recebimento', 0.0),
    ('valor_valor_declarado', 0.0),
    ('entrega_domiciliar', True),
    ('entrega_sabado', True),
    ('erro', 0),
    ('msg_erro', None)
)

@Vows.batch
class ServiceVows(Vows.Context):

    class WhenInitialized(Vows.Context):

        class WhenValidArgumentsArePassed(Vows.Context):

            def topic(self):
                service = Service(**dict(TEST_CASES))

                for attribute, value in TEST_CASES:
                    yield (service, attribute, value)

            def it_assign_attributes_values(self, topic):
                service, attribute, value = topic
                expect(getattr(service, attribute)).to_equal(value)

        class WhenInvalidArgumentsArePassed(Vows.Context):

            def topic(self):
                return Service(invalid_kwargs=None)

            def it_raises_type_error(self, topic):
                expect(topic).to_be_an_error_like(TypeError)

    class CreateFromSudsObject(Vows.Context):

        def topic(self):
            suds_object = create_sudsobject_mock()
            service = Service.create_from_suds_object(suds_object)

            for attribute, value in TEST_CASES:
                yield (service, attribute, value)

        def returns_a_service_instance_with_attributes_correctly_coersed(self,
                topic):
            service, attribute, value = topic
            expect(getattr(service, attribute)).to_equal(value)
