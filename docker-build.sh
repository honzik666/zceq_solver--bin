#!/bin/sh

IMAGE=docker.bo/pool/main/base-env

docker run -v `pwd`:/build -w /build -v `pwd`/.local:/.local -v `pwd`/.cache:/.cache -u `id -u` $IMAGE bash -c "\
rm dist/* venv/* -rf && \
mkdir venv -p && \
virtualenv venv/py2.7 -p \`which python2.7\` && \
venv/py2.7/bin/pip install -e . && \
venv/py2.7/bin/pip install wheel && \
venv/py2.7/bin/python ./setup.py bdist_wheel && \
python3.6 -m venv venv/py3.6 && \
venv/py3.6/bin/pip install -e . && \
venv/py3.6/bin/pip install wheel && \
venv/py3.6/bin/python ./setup.py bdist_wheel && \
python3.7 -m venv venv/py3.7 && \
venv/py3.7/bin/pip install -e . && \
venv/py3.7/bin/pip install wheel && \
venv/py3.7/bin/python ./setup.py bdist_wheel
virtualenv venv/pypy -p \`which pypy\` && \
venv/pypy/bin/pip install -e . && \
venv/pypy/bin/pip install wheel && \
venv/pypy/bin/python ./setup.py bdist_wheel

"
