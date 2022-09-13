#! /usr/bin/env python
from __future__ import print_function

import pip
from setuptools import setup, Extension


def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])


install("cython==0.29.32")
install("numpy==1.23.3")


import numpy as np
from Cython.Build import cythonize


DISTNAME = 'lsh'
DESCRIPTION = 'A library for performing shingling and LSH for python.'

MAINTAINER = 'Matti Lyra'
MAINTAINER_EMAIL = 'matti.lyra@gmail.com'
URL = 'https://github.com/mattilyra/lsh'
DOWNLOAD_URL = 'https://github.com/mattilyra/lsh'

VERSION = '0.3.0'

includes = [np.get_include()]
extensions = [
    Extension(
        "lsh.cMinhash",
        ["lsh/cMinhash.pyx", 'lsh/MurmurHash3.cpp'],
        include_dirs=includes
    ),
    Extension(
        "lsh.utils",
        ["lsh/utils.pyx"],
        include_dirs=includes
    )
]
extensions = cythonize(extensions, force=True)

install_deps = ['numpy', 'cython>=0.24.1']
test_deps = ['coverage>=4.0.3', 'pytest>=3.0', ]
setup(name=DISTNAME,
      version=VERSION,
      description=DESCRIPTION,
      author=MAINTAINER,
      author_email=MAINTAINER_EMAIL,
      url=URL,
      packages=['lsh'],
      ext_modules=extensions,
      install_requires=install_deps,
      tests_require=test_deps)
