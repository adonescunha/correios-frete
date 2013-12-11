#!/usr/bin/env python
# -*- coding: utf-8 -*-

# correios-frete
# https://github.com/adonescunha/correios-frete

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Adones Cunha adonescunha@gmail.com


from pyvows import Vows, expect

from correios_frete import Package, Service
from correios_frete.client import Client
from correios_frete.constants import SEDEX, PAC


@Vows.batch
class IntegrationVows(Vows.Context):

    def topic(self):
        client = Client(cep_origem='01310-200')
        package = Package()
        package.add_item(
            weight=0.5,
            height=6.0,
            width=16.0,
            length=16.0
        )
        result = client.calc_preco_prazo(package, '52020-010', SEDEX, PAC)

        for code, service in zip([SEDEX, PAC], result):
            yield code, service

    def it_returns_service_instances(self, topic):
        code, service = topic
        expect(service.codigo).to_equal(code)
