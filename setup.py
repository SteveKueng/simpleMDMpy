#!/usr/bin/env python

import os
import re
import sys

from codecs import open

from setuptools import setup

packages = ['simpleMDMpy']

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, 'simpleMDMpy', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=packages,
    package_dir={'simpleMDMpy': 'simpleMDMpy'},
    include_package_data=True,
    #install_requires=requires,
    zip_safe=False,
)

