#!/bin/bash

let BEGIN=${1}
FILE="$3"
LAST_LINE=$(nl $FILE | tail -1 | sed 's,^[[:blank:]]\+\([[:digit:]]\+\)[[:blank:]]\+[[:digit:]]\+[[:space:]]*$,\1,')

if [ $2 -lt $LAST_LINE ]
then
    let END=${2}
    let PRINT=${2}
else
    let END=${LAST_LINE}
    let PRINT=${LAST_LINE}
fi

if [ $END -eq $LAST_LINE ]
then
    sed -n ':begin '"$BEGIN"','"$END"' {'"$PRINT"'p; N; s/[[:space:]]*\n/, /; b begin}' $FILE
else
    sed -n ':begin '"$BEGIN"','"$END"' {'"$PRINT"'p; N; s/[[:space:]]*\n/, /; b begin}' $FILE | sed 's/$/,/'
fi

exit 0

