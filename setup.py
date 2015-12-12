#!/usr/bin/env python

import setuptools
from distutils.core import setup

setup(
    name = 'dwgstrings',
    version = '0.1',
    packages = ['dwgstrings'],
    entry_points = {
        'console_scripts': [
            'dwgstrings = dwgstrings.__main__:main'
        ]
    }
)
