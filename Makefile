SHELL := /bin/bash

VIRTUAL_ENV = "./venv/bin/python"
MY_PYTHON = `which python3.7`

install:
	${MY_PYTHON} -m venv venv;
	${VIRTUAL_ENV} setup.py install
	${VIRTUAL_ENV} setup.py dev_install
