#!/bin/bash

rm -rf ~/.local/venvs/sistec_download
python3.11 -m venv ~/.local/venvs/sistec_download
. ~/.local/venvs/sistec_download/bin/activate
python3.11 -m pip install -U pep517
python3.11 -m pip install --use-pep517 -U pip
python3.11 -m pip install --use-pep517 -U -r requirements.txt

exit 0
