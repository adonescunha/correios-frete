#!/usr/bin/env python
# -*- coding: utf-8 -*-

# correios-frete
# https://github.com/adonescunha/correios-frete

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Adones Cunha adonescunha@gmail.com


from setuptools import setup

from correios_frete import version


setup(
    name='correios-frete',
    version=version.to_str(),
    description='Cliente para o WebService de consulta de frete dos correios.',
    author='Adones Cunha',
    author_email='adonescunha@gmail.com',
    url='https://github.com/adonescunha/correios-frete',
    packages=[
        'correios_frete'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=[
        'suds'
    ]
)
