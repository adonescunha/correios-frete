#!/usr/bin/env python
# -*- coding: utf-8 -*-

# correios-frete
# https://github.com/adonescunha/correios-frete

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Adones Cunha adonescunha@gmail.com


from pyvows import Vows, expect
from mock import Mock

import correios_frete
from correios_frete import Client, Package
from correios_frete.constants import WSDL_URL, CAIXA_PACOTE, SEDEX, PAC

@Vows.batch
class ClientVows(Vows.Context):

    class WhenInitialized(Vows.Context):

        class WithoutCEPOrigem(Vows.Context):

            def topic(self):
                return Client()

            def its_raises_an_error(self, topic):
                expect(topic).to_be_an_error_like(TypeError)

        class WithCEPOrigem(Vows.Context):

            def teardown(self):
                import suds
                correios_frete.client.SudsClient = suds.client.Client

            def topic(self):
                correios_frete.client.SudsClient = Mock()

                cep_origem = '00000-000'
                kwargs = [
                    ('codigo_empresa', ''),
                    ('senha', ''),
                    ('valor_declarado', 0.0),
                    ('mao_propria', False),
                    ('aviso_recebimento', False)
                ]
                client = Client(cep_origem=cep_origem)

                return (cep_origem, kwargs, client)

            def it_assigns_cep_origem(self, topic):
                cep_origem, _, client = topic
                expect(client.cep_origem).to_equal(cep_origem)

            def it_assigns_a_suds_client(self, topic):
                correios_frete.client.SudsClient.assert_called_with(WSDL_URL)

            class ItAssigns(Vows.Context):

                def topic(self, topic):
                    _, kwargs, client = topic

                    for attribute, value in kwargs:
                        yield (attribute, value, client)

                def default_attribute_values(self, topic):
                    attribute, value, client = topic
                    expect(getattr(client, attribute)).to_equal(value)

    class BuildWebServiceCallArgs(Vows.Context):

        def topic(self):
            cep_origem  = '00000-000'
            cep_destino = '11111-111'
            client = Client(cep_origem=cep_origem)
            package = Package()
            package.add_item(weight=1, height=2, width=3, length=4)

            expected = (
                '',            # nCdEmpresa
                '',            # sDsSenha
                '40010,41106', # nCdServico
                cep_origem,    # sCepOrigem
                cep_destino,   # sCepDestino
                1,             # nVlPeso
                CAIXA_PACOTE,  # nCdFormato
                4,             # nVlComprimento
                2,             # nVlAltura
                3,             # nVlLargura
                0,             # nVlDiametro
                False,         # sCdMaoPropria
                0.0,           # nVlValorDeclarado
                False          # sCdAvisoRecebimento
            )

            result = client.build_web_service_call_args(package, cep_destino,
                    *(SEDEX, PAC))

            for expected_value, actual_value in zip(expected, result):
                yield (expected_value, actual_value)

        def returns_args_in_correct_order(self, topic):
            expected, actual = topic
            expect(expected).to_equal(actual)

    class CallWebService(Vows.Context):

        def topic(self):
            cep_origem  = '00000-000'
            cep_destino = '11111-111'
            method_name = 'methodName'
            args = (1, 2, 3)
            client = Client(cep_origem=cep_origem)
            package = Package()
            services = (SEDEX, PAC)
            client.build_web_service_call_args = Mock(return_value=args)
            client.ws_client.service = Mock()
            client.call_web_service(method_name, package, cep_destino,
                    *services)

            return (method_name, package, cep_destino, services, args, client)

        def build_call_args(self, topic):
            _, package, cep_destino, services, _, client = topic
            client.build_web_service_call_args.assert_called_with(package,
                    cep_destino, *services)

        def calls_provided_method(self, topic):
            method_name, _, _, _, args, client = topic
            getattr(client.ws_client.service, method_name)\
                    .assert_called_with(*args)
