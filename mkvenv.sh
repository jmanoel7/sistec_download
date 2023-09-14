#!/bin/bash
set -e

# to install pyenv execute the following:
# -----BEGIN PYENV INSTALL-----
# curl https://pyenv.run | bash
# cat >>~/.bashrc<<EOF
# export PYENV_ROOT="$HOME/.pyenv"
# command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
# eval "$(pyenv init -)"
# eval "$(pyenv virtualenv-init -)"
# EOF
# # re-open terminal and execute the following:
# cd ~
# sudo apt update; sudo apt install build-essential libssl-dev zlib1g-dev \
#   libbz2-dev libreadline-dev libsqlite3-dev curl \
#   libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
# pyenv install 3.11
# pyenv local 3.11
# -----END PYENV INSTALL-----

# to install virtualenv sistec_download execute the following:
# -----BEGIN VIRTUALENV INSTALL-----
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
rm -f "$PWD/.python-version"
pyenv deactivate sistec_download
pyenv shell 3.11
pyenv virtualenv-delete -f sistec_download
pyenv virtualenv sistec_download
pyenv activate sistec_download
python3.11 -m pip install -U pep517
python3.11 -m pip install --use-pep517 -U pip
python3.11 -m pip install --use-pep517 -U -r requirements.txt
pyenv local sistec_download
# -----END VIRTUALENV INSTALL-----

exit 0
