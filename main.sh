#!/bin/bash
set -e

FILE_FACE_TO_FACE_COD_IN="$1"
A="$(dirname $FILE_FACE_TO_FACE_COD_IN)"
B="$(basename $FILE_FACE_TO_FACE_COD_IN .txt)"
FILE_FACE_TO_FACE_COD_OUT="${A}/${B}-sort.txt"

# python3.11 make list course codes from spreadsheets csv
#python3.11 ./make-list-course-codes.py $FILE_FACE_TO_FACE_COD_IN

# sort course codes
sort -n -u $FILE_FACE_TO_FACE_COD_IN > $FILE_FACE_TO_FACE_COD_OUT

# insert lines with course codes within tweak_face-to-face_spreadsheets.py
./make-lines-course-codes.sh $FILE_FACE_TO_FACE_COD_OUT | sed -i '/\#test1/,/\#test2/ r /dev/stdin' tweak_face-to-face_spreadsheets.py


