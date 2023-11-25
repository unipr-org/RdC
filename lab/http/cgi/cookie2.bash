#!/bin/bash

#################################

function setcookie()
        #
        # $1 = nome variabile
        # $2 = valore variabile
        # $3 = durata (secondi)
        # $4 = path (opzionale)
        #
{
value=$( echo -n "$2" | ./urlencode )
#value=$( echo -n "$2" )
if [ -z "$4" ]; then
  path=""
else
    path="; Path=$4"
fi
echo -n "Set-Cookie: $1=$value$path; expires="
date -u --date="$3 seconds" "+%a, %d-%b-%y %H:%M:%S GMT"
}

#################################################

function get_parameter ()
{
echo "$QUERY_STRING" | tr '&' '\n' | grep "^$1=" | head -1 | sed "s/.*=//" 
}

#################################################

if [  -z $QUERY_STRING ]; then 
cat << EOF
Content-Type: text/html

<hr>
<a href="http://${SERVER_NAME}${SCRIPT_NAME}"> ${SCRIPT_NAME} </a> <p>
<hr>
<form  action="http://${SERVER_NAME}${SCRIPT_NAME}" method="GET" />
<input type="text"  NAME="NOME"    VALUE="NOME"    SIZE="20" MAXLENGTH="20" />
<input type="text"  NAME="COGNOME" VALUE="COGNOME" SIZE="20" MAXLENGTH="20" />
<input type="text"  NAME="CODICE"  VALUE="CODICE"  SIZE="20" MAXLENGTH="20" />
<input type="submit" VALUE="    Ok    ">
</form>
EOF

else

NOME=$(get_parameter NOME)
COGNOME=$(get_parameter COGNOME)
CODICE=$(get_parameter CODICE)

# 600 sec (10 min)
echo "Content-Type: text/html"
setcookie Nome      $NOME    600
setcookie Cognome   $COGNOME 600
setcookie Codice    $CODICE  600
echo
cat << EOF
<hr>
<a href="http://${SERVER_NAME}${SCRIPT_NAME}"> ${SCRIPT_NAME} </a> <p>
<hr>
NOME: $NOME - 
COGNOME: $COGNOME - 
CODICE: $CODICE

<hr>
EOF

fi
        

