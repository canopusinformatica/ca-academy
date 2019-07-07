#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import distutils.cmd
from setuptools import find_packages, setup

CURRENT_PYTHON_VERSION = sys.version_info[:2]
REQUIRED_PYTHON_VERSION = (3, 5)
REQUIREMENTS = []

if CURRENT_PYTHON_VERSION < REQUIRED_PYTHON_VERSION:
    sys.stderr.write("""
==========================
Unsupported Python version
==========================
This version of Django requires Python {}.{}, but you're trying to install iton Python {}.{}
""".format(*(REQUIRED_PYTHON_VERSION + CURRENT_PYTHON_VERSION)))
    sys.exit(1)


class PrecommitCommand(distutils.cmd.Command):
    """
    Classe utilitária para instalar a ferramenta de pré commit
    execute python setup.py pre_commit após rodar python setup.py install
    """

    user_options = []
    description = 'Execute python setup.py pre_commit para instalar'

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.install_development_packages('server/requirements-dev.txt')
        os.system('pre-commit install')

    def install_development_packages(self, name):
        try:
            import subprocess
            subprocess.call(['pip', 'install', '-r', name])
        except ImportError:
            print("Módulo não encontrado")


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        if os.path.splitext(fname)[-1] == '.txt':
            return f.read().splitlines()
        return f.read()


setup(
    name='canopus-academy',
    version='0.0.1',
    python_requires='>={}.{}'.format(*REQUIRED_PYTHON_VERSION),
    author='Níkolas Vargas',
    author_email='vargasnikolass@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        read('server/requirements.txt')
    ],
    cmdclass={
        'pre_commit': PrecommitCommand
    },
    long_description=read('README.md')
)
