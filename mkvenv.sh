#!/bin/bash
set -e
mkdir -p ${HOME}/.local/venv/
virtualenv -p /usr/bin/python3 ${HOME}/.local/venv/sistec_download_automatico
source ${HOME}/.local/venv/sistec_download_automatico/bin/activate
pip install -U pip
pip install -U -r ${PWD}/requirements.txt
exit 0
