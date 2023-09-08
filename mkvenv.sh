#!/bin/bash
set -e
# # to install pyenv execute the following:
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
pyenv shell 3.11
pyenv virtualenv-delete -f sistec_download
pyenv virtualenv sistec_download
pyenv local sistec_download
pyenv activate sistec_download
python3.11 -m pip install -U pip
python3.11 -m pip install -U -r requirements.txt
exit 0
