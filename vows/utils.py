#!/usr/bin/env python
# -*- coding: utf-8 -*-

# correios-frete
# https://github.com/adonescunha/correios-frete

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Adones Cunha adonescunha@gmail.com


from mock import Mock


def create_sudsobject_mock():
    return Mock(
        Codigo=40010,
        Valor='71,00',
        PrazoEntrega='1',
        ValorMaoPropria='0,00',
        ValorAvisoRecebimento='0,00',
        ValorValorDeclarado='0,00',
        EntregaDomiciliar='S',
        EntregaSabado='S',
        Erro='0',
        MsgErro=None
    )
