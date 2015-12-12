#!/usr/bin/env python

from setuptools import setup

setup(
    name = 'dwgstrings',
    version = '0.1',
    packages = ['dwgstrings'],
    install_requires = ['dxfgrabber'],
    entry_points = {
        'console_scripts': [
            'dwgstrings = dwgstrings.__main__:main'
        ]
    },

    license = "MIT"
)
