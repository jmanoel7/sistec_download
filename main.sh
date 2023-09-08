#!/bin/bash
set -e

# create virtualenv 'sistec_download'
./mkvenv.sh

DIR_BASE="./sistec_cod_cursos/"

FILE_CODE_IN="${DIR_BASE}/codes.txt"
FILE_CODE_OUT="${DIR_BASE}/codes_sort.txt"

FILE_EAD_CODE_IN="${DIR_BASE}/codes_ead.txt"
FILE_EAD_CODE_OUT="${DIR_BASE}/codes_ead_sort.txt"

rm -rf $DIR_BASE
mkdir -p $DIR_BASE

# python3.11 bot get course codes from sistec.mec.gov.br
python3.11 ./bot_get_course_codes.py

# python3.11 make list course codes from spreadsheets csv
python3.11 ./make-list-course-codes.py

# sort course codes
sort -n -u $FILE_CODE_IN > $FILE_CODE_OUT
sort -n -u $FILE_EAD_CODE_IN > $FILE_EAD_CODE_OUT

# separation of distance course codes
python3.11 ./separation-course-codes.py
FILE_EAD_ONE_CODE_OUT="${DIR_BASE}/codes_ead_one_sort.txt"
FILE_EAD_TWO_CODE_OUT="${DIR_BASE}/codes_ead_two_sort.txt"

# insert lines with course codes within tweak_spreadsheets.py
sed -i '/\# -----BEGIN DISTANCE COURSE CODES-----/,/\# -----END DISTANCE COURSE CODES-----/ r '<(./make-lines-course-codes.sh $FILE_EAD_TWO_CODE_OUT) tweak_spreadsheets.py
sed -i '/\# -----BEGIN FACE-TO-FACE COURSE CODES-----/,/\# -----END FACE-TO-FACE COURSE CODES-----/ r '<(./make-lines-course-codes.sh $FILE_CODE_OUT) tweak_spreadsheets.py

# insert lines with course codes within tweak_ead_spreadsheets.py
sed -i '/\# -----BEGIN DISTANCE COURSE CODES-----/,/\# -----END DISTANCE COURSE CODES-----/ r '<(./make-lines-course-codes.sh $FILE_EAD_ONE_CODE_OUT) tweak_ead_spreadsheets.py

# yapf tweak_spreadsheets.py and tweak_ead_spreadsheets.py


# python3.11 bot get spreadsheets from sistec.mec.gov.br


# execute tweaks ...

