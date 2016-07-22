#!/usr/bin/env python

from distutils.core import setup

from gearman import __version__ as version

setup(
    name = 'gearman',
    version = version,
    description = '',
    packages = ['gearman'],
)
