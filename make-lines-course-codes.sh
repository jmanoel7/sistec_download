#!/bin/bash

SPACES="$1"
FILE="$2"
LAST_LINE=$(nl $FILE | tail -1 | sed 's,^[[:blank:]]\+\([[:digit:]]\+\)[[:blank:]]\+[[:digit:]]\+[[:space:]]*$,\1,')

for ((i=1; i<=${LAST_LINE}; i+=5))
do

    let a=${i}
    let b=${i}+4

    if [ $SPACES -eq 16 ]
    then
        ./join-lines-with-comma.sh $a $b $FILE | sed 's,^,                ,'
    elif [ $SPACES -eq 12 ]
    then
        ./join-lines-with-comma.sh $a $b $FILE | sed 's,^,            ,'
    fi

done

exit 0

