# -*- coding: utf-8 -*-

from __future__ import absolute_import

import io
import os
import re
import sys
import codecs
from setuptools import setup
from setuptools.command.test import test as TestCommand


rootpath = os.path.abspath(os.path.dirname(__file__))


class PyTest(TestCommand):
    """python setup.py test"""
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--strict', '--verbose', '--tb=long', 'tests']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


def read(*parts):
    return open(os.path.join(rootpath, *parts), 'r').read()


def extract_version():
    version = None
    fname = os.path.join(rootpath, 'gsw', '__init__.py')
    with open(fname) as f:
        for line in f:
            if (line.startswith('__version__')):
                _, version = line.split('=')
                version = version.strip()[1:-1]  # Remove quotation characters
                break
    return version


email = "ocefpaf@gmail.com"
maintainer = "Filipe Fernandes"
authors = ['Eric Firing', u'Bjørn Ådlandsvik', 'Filipe Fernandes']

LICENSE = read('LICENSE.txt')
long_description = '{}\n{}'.format(read('README.txt'), read('CHANGES.txt'))

config = dict(name='gsw',
              version=extract_version(),
              packages=['gsw', 'gsw/gibbs', 'gsw/utilities', 'gsw/test'],
              package_data={'gsw': ['utilities/data/*.npz']},
              tests_require=['pytest', 'scipy', 'oct2py'],
              cmdclass=dict(test=PyTest),
              license=LICENSE,
              long_description=long_description,
              classifiers=['Development Status :: 4 - Beta',
                           'Environment :: Console',
                           'Intended Audience :: Science/Research',
                           'Intended Audience :: Developers',
                           'Intended Audience :: Education',
                           'License :: OSI Approved :: MIT License',
                           'Operating System :: OS Independent',
                           'Programming Language :: Python',
                           'Topic :: Education',
                           'Topic :: Scientific/Engineering',
                           ],
              description='Gibbs Seawater Oceanographic Package of TEOS-10',
              author=authors,
              author_email=email,
              maintainer=maintainer,
              maintainer_email=email,
              url='http://pypi.python.org/pypi/seawater/',
              download_url='https://pypi.python.org/pypi/gsw/',
              platforms='any',
              keywords=['oceanography', 'seawater', 'TEOS-10', 'gibbs'],
              install_requires=['numpy'],
              extras_require=dict(testing=['pytest'])
              )

setup(**config)
