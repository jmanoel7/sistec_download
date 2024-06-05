#!/bin/bash
set -e


# create virtualenv
./mkvenv.sh


# activate virtualenv
. ~/.local/venvs/sistec_download/bin/activate


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


# create folders for course codes to all campi
python ./create_folders_course_codes.py


echo -e '\nPronto! Agora você já pode baixar as planilhas com os códigos dos cursos direto do sistec!'
echo -e 'Baixe cada planilha e mova-a para a sua devida pasta (de acordo com o nome do campus).'
echo -e "A raiz onde as pastas (campus) ficam é: ${DIR_BASE} ."

opt="0"
while [[ "$opt" != "s" ]] && [[ "$opt" != "S" ]] && [[ "$opt" != "n" ]] && [[ "$opt" != "N" ]]
do
    echo -e '\nJá baixou as TODAS as planilhas e as colocou em suas devidas pastas? (S/N)?'
    read opt
done

if [[ "$opt" = "N" ]] || [[ "$opt" = "n" ]]
then
    echo "Não se esqueça de continuar o código de onde parou se for o caso,"
    echo "aí altere momentaneamente o arquivo campus.py e depois restaure-o com o all_campus.py !"
    exit 0
fi


python make list course codes from spreadsheets csv
python ./make-list-course-codes.py


sort course codes
sort -n -u $FILE_CODE_IN > $FILE_CODE_OUT
sort -n -u $FILE_EAD_CODE_IN > $FILE_EAD_CODE_OUT


separation of distance course codes
python ./separation-course-codes.py


delete lines with old course codes in tweak_spreadsheets.py
sed -i '/\# -----BEGIN DISTANCE COURSE CODES-----/,/\# -----END DISTANCE COURSE CODES-----/ { /\# -----BEGIN DISTANCE COURSE CODES-----/ b; /\# -----END DISTANCE COURSE CODES-----/ b; d }' tweak_spreadsheets.py
sed -i '/\# -----BEGIN FACE-TO-FACE COURSE CODES-----/,/\# -----END FACE-TO-FACE COURSE CODES-----/ { /\# -----BEGIN FACE-TO-FACE COURSE CODES-----/ b; /\# -----END FACE-TO-FACE COURSE CODES-----/ b; d }' tweak_spreadsheets.py


insert lines with new course codes in tweak_spreadsheets.py
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


# create folders for spreadsheets to all campi
python ./create_folders_spreadsheets.py


echo -e '\nPronto! Agora você já pode baixar as planilhas com os alunos direto do sistec!'
echo -e 'Baixe cada planilha e mova-a para a sua devida pasta (de acordo com o nome do campus).'
echo -e "A raiz onde as pastas (campus) ficam é: ${DIR_AUDIT} ."

opt="0"
while [[ "$opt" != "s" ]] && [[ "$opt" != "S" ]] && [[ "$opt" != "n" ]] && [[ "$opt" != "N" ]]
do
    echo -e '\nJá baixou as TODAS as planilhas e as colocou em suas devidas pastas? (S/N)?'
    read opt
done

if [[ "$opt" = "N" ]] || [[ "$opt" = "n" ]]
then
    echo "Não se esqueça de continuar o código de onde parou se for o caso,"
    echo "aí altere momentaneamente o arquivo campus.py e depois restaure-o com o all_campus.py !"
    exit 0
fi


# create files from spreadsheets to all campi
python ./create_files_spreadsheets.py


# execute tweaks in spreadsheets
cd ./sistec_audit/presencial/
python ../../tweak_spreadsheets.py
cd ../..

cd ./sistec_audit/ead/
python ../../tweak_ead_spreadsheets.py
cd ../..


exit 0
