#!/usr/bin/env python

import os

from codecs import open
from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, 'simpleMDMpy', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

setup(
  name = 'simpleMDMpy',
  packages = ['simpleMDMpy'],
  version=about['__version__'],
  description=about['__description__'],
  author=about['__author__'],
  author_email=about['__author_email__'],
  url = 'https://github.com/SteveKueng/simpleMDMpy',
  keywords = ['SimpleMDM'], 
  classifiers = [],
)