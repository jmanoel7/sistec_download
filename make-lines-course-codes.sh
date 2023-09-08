#!/bin/bash

FILE="$1"
LAST_LINE=$(nl $FILE | tail -1 | sed 's,^[[:blank:]]\+\([[:digit:]]\+\)[[:blank:]]\+[[:digit:]]\+[[:space:]]*$,\1,')

for ((i=1; i<=${LAST_LINE}; i+=5))
do

    let a=${i}
    let b=${i}+4
    ./join-lines-with-comma.sh $a $b $FILE

done

exit 0
