#!/bin/bash
set -e


# create and use virtualenv 'sistec_download'
./mkvenv.sh
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"


# export vars
export DIR_AUDIT="${PWD}/sistec_audit"
export DIR_BASE="${PWD}/sistec_course_codes"
export FILE_CODE_IN="${DIR_BASE}/codes.txt"
export FILE_CODE_OUT="${DIR_BASE}/codes_sort.txt"
export FILE_EAD_CODE_IN="${DIR_BASE}/codes_ead.txt"
export FILE_EAD_CODE_OUT="${DIR_BASE}/codes_ead_sort.txt"
export FILE_EAD_ONE_CODE_OUT="${DIR_BASE}/codes_ead_one_sort.txt"
export FILE_EAD_TWO_CODE_OUT="${DIR_BASE}/codes_ead_two_sort.txt"
export GIT_PROJECT_PATH="${HOME}/git/ifg/sistec_download"


# clean and mkdir dir_base
rm -rf "$DIR_BASE"
mkdir -p "$DIR_BASE"


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


# delete lines with old course codes in tweak_spreadsheets.py
sed -i '/\# -----BEGIN DISTANCE COURSE CODES-----/,/\# -----END DISTANCE COURSE CODES-----/ { /\# -----BEGIN DISTANCE COURSE CODES-----/ b; /\# -----END DISTANCE COURSE CODES-----/ b; d }' tweak_spreadsheets.py
sed -i '/\# -----BEGIN FACE-TO-FACE COURSE CODES-----/,/\# -----END FACE-TO-FACE COURSE CODES-----/ { /\# -----BEGIN FACE-TO-FACE COURSE CODES-----/ b; /\# -----END FACE-TO-FACE COURSE CODES-----/ b; d }' tweak_spreadsheets.py


# insert lines with new course codes in tweak_spreadsheets.py
./make-lines-course-codes.sh 16 $FILE_EAD_TWO_CODE_OUT | \
    sed -i '/\# -----BEGIN DISTANCE COURSE CODES-----/,/\# -----END DISTANCE COURSE CODES-----/ r /dev/stdin' tweak_spreadsheets.py
./make-lines-course-codes.sh 16 $FILE_CODE_OUT | \
    sed -i '/\# -----BEGIN FACE-TO-FACE COURSE CODES-----/,/\# -----END FACE-TO-FACE COURSE CODES-----/ r /dev/stdin' tweak_spreadsheets.py


# delete lines with old course codes in tweak_ead_spreadsheets.py
sed -i '/\# -----BEGIN DISTANCE COURSE CODES-----/,/\# -----END DISTANCE COURSE CODES-----/ { /\# -----BEGIN DISTANCE COURSE CODES-----/ b; /\# -----END DISTANCE COURSE CODES-----/ b; d }' tweak_ead_spreadsheets.py


# insert lines with new course codes in tweak_ead_spreadsheets.py
./make-lines-course-codes.sh 12 $FILE_EAD_ONE_CODE_OUT | \
    sed -i '/\# -----BEGIN DISTANCE COURSE CODES-----/,/\# -----END DISTANCE COURSE CODES-----/ r /dev/stdin' tweak_ead_spreadsheets.py


# clean and mkdir dir_audit
rm -rf "$DIR_AUDIT"
mkdir -p "$DIR_AUDIT"


# clean sistec*.csv from user's home
rm -f ~/Downloads/sistec*.csv


# python3.11 bot get spreadsheets from sistec.mec.gov.br
./bot_get_spreadsheets.py


# execute tweaks in spreadsheets
cd ./sistec_audit/presencial/
../../tweak_spreadsheets.py
cd ../..

cd ./sistec_audit/ead/
../../tweak_ead_spreadsheets.py
cd ../..


exit 0
