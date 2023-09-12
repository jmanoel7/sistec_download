#!/bin/bash

deactivate >/dev/null 2>&1
rm -rf ~/.local/venvs/sistec_download
mkdir -p ~/.local/venvs
python3.11 -m venv ~/.local/venvs/sistec_download
. ~/.local/venvs/sistec_download/bin/activate
python3.11 -m pip install --no-cache-dir -U pep517
python3.11 -m pip install --no-cache-dir --use-pep517 -U pip
python3.11 -m pip install --no-cache-dir --use-pep517 -r requirements.txt

exit 0
