#!/bin/bash

# clean virtualenv
deactivate >/dev/null 2>&1
rm -rf ~/.local/venvs/sistec_download

# creat virtualenv
python -m venv ~/.local/venvs/sistec_download

# activate virtualenv
. ~/.local/venvs/sistec_download/bin/activate

# install pip packages
pip install -U pip
pip install -U -r requirements.txt

exit 0
