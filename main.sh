#!/bin/bash
set -e

# create and use virtualenv 'sistec_download'
# ./mkvenv.sh
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
pyenv shell 3.11
pyenv local sistec_download
pyenv activate sistec_download

# export vars
export DIR_BASE="${PWD}/sistec_course_codes"
export FILE_CODE_IN="${DIR_BASE}/codes.txt"
export FILE_CODE_OUT="${DIR_BASE}/codes_sort.txt"
export FILE_EAD_CODE_IN="${DIR_BASE}/codes_ead.txt"
export FILE_EAD_CODE_OUT="${DIR_BASE}/codes_ead_sort.txt"
export FILE_EAD_ONE_CODE_OUT="${DIR_BASE}/codes_ead_one_sort.txt"
export FILE_EAD_TWO_CODE_OUT="${DIR_BASE}/codes_ead_two_sort.txt"
export GIT_PROJECT_PATH="${HOME}/git/ifg/sistec_download"

# clean and mkdir dirbase
# rm -rf "$DIR_BASE"
# mkdir -p "$DIR_BASE"

# clean sistec_csv* and cursos_tecnicos* from user's home
rm -f ~/Downloads/sistec_csv*
rm -f ~/Downloads/cursos_tecnicos*

# python3.11 bot get course codes from sistec.mec.gov.br
./bot_get_course_codes.py

# python3.11 make list course codes from spreadsheets csv
./make-list-course-codes.py

# sort course codes
sort -n -u $FILE_CODE_IN > $FILE_CODE_OUT
sort -n -u $FILE_EAD_CODE_IN > $FILE_EAD_CODE_OUT

# separation of distance course codes
./separation-course-codes.py

# insert lines with course codes within tweak_spreadsheets.py
sed -i '/\# -----BEGIN DISTANCE COURSE CODES-----/,/\# -----END DISTANCE COURSE CODES-----/ r '<(./make-lines-course-codes.sh $FILE_EAD_TWO_CODE_OUT) tweak_spreadsheets.py
sed -i '/\# -----BEGIN FACE-TO-FACE COURSE CODES-----/,/\# -----END FACE-TO-FACE COURSE CODES-----/ r '<(./make-lines-course-codes.sh $FILE_CODE_OUT) tweak_spreadsheets.py

# insert lines with course codes within tweak_ead_spreadsheets.py
sed -i '/\# -----BEGIN DISTANCE COURSE CODES-----/,/\# -----END DISTANCE COURSE CODES-----/ r '<(./make-lines-course-codes.sh $FILE_EAD_ONE_CODE_OUT) tweak_ead_spreadsheets.py

# yapf tweak_spreadsheets.py and tweak_ead_spreadsheets.py


# python3.11 bot get spreadsheets from sistec.mec.gov.br
#./bot_get_spreadsheets.py

# execute tweaks ...


exit 0
