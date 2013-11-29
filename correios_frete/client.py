#!/usr/bin/env python
# -*- coding: utf-8 -*-

# correios-frete
# https://github.com/adonescunha/correios-frete

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Adones Cunha adonescunha@gmail.com


from suds.client import Client as SudsClient

from .constants import WSDL_URL
from .service import Service


def web_service_call(method_name):
    def wrapper(self, package, cep_destino, *services):
        return self.call_web_service(method_name, package, cep_destino,
                *services)

    return wrapper


class Client(object):

    def __init__(self, cep_origem, codigo_empresa='', senha='',
            valor_declarado=0.0, mao_propria=False, aviso_recebimento=False):
        self.cep_origem = cep_origem
        self.codigo_empresa = codigo_empresa
        self.senha = senha
        self.valor_declarado = valor_declarado
        self.mao_propria = mao_propria
        self.aviso_recebimento = aviso_recebimento

    @property
    def ws_client(self):
        if not hasattr(self, '_ws_client'):
            self._ws_client = SudsClient(WSDL_URL)

        return self._ws_client

    def build_web_service_call_args(self, package, cep_destino, *services):
        return (
            self.codigo_empresa,   # nCdEmpresa
            self.senha,            # sDsSenha
            ','.join(services),    # nCdServico
            self.cep_origem,       # sCepOrigem
            cep_destino,           # sCepDestino
            package.weight,        # nVlPeso
            package.formato,       # nCdFormato
            package.length,        # nVlComprimento
            package.height,        # nVlAltura
            package.width,         # nVlLargura
            0,                     # nVlDiametro
            self.mao_propria,      # sCdMaoPropria
            self.valor_declarado,  # nVlValorDeclarado
            self.aviso_recebimento # sCdAvisoRecebimento
        )

    def call_web_service(self, method_name, package, cep_destino, *services):
        args = self.build_web_service_call_args(package, cep_destino, *services)
        result = getattr(self.ws_client.service, method_name)(*args)

        return [Service.create_from_suds_object(result.Servicos[0][i])
                for i in range(len(result.Servicos[0]))]

    calc_preco_data       = web_service_call('CalcPrecoData')

    calc_preco_prazo      = web_service_call('CalcPrecoPrazo')

    calc_prazo            = web_service_call('CalcPrazo')

    calc_preco            = web_service_call('CalcPreco')

    calc_prezo_prazo_data = web_service_call('CalcPrezoPrazoData')

    calc_prazo_data       = web_service_call('CalcPrecoData')
