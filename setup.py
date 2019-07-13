#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import distutils.cmd
from setuptools import find_packages, setup
from pathlib import Path

CURRENT_PYTHON_VERSION = sys.version_info[:2]
REQUIRED_PYTHON_VERSION = (3, 5)
REQUIREMENTS = []

if CURRENT_PYTHON_VERSION < REQUIRED_PYTHON_VERSION:
    sys.stderr.write("""
==========================
Unsupported Python version
==========================
Essa versão do Django requer Python >= {}.{}, mas você está tentando instalar usando Python {}.{}
Por acaso esqueceu de ativar o seu ambiente virtual?
""".format(*(REQUIRED_PYTHON_VERSION + CURRENT_PYTHON_VERSION)))
    sys.exit(1)


class PrecommitCommand(distutils.cmd.Command):
    """
    Classe utilitária para instalar a ferramenta de pré commit
    """

    user_options = []
    description = 'Use make install'
    env_path = str(Path('venv/bin').resolve())
    pip_path = f"{env_path}/pip"
    pre_commit_path = f"{env_path}/pre-commit"

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.install_development_packages('server/requirements-dev.txt')
        os.system(f"{self.pre_commit_path} install")

    def install_development_packages(self, name):
        try:
            import subprocess
            subprocess.call([self.pip_path, 'install', '-r', name])
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
        'dev_install': PrecommitCommand
    },
    long_description=read('README.md')
)
