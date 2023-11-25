#!/bin/bash

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


function get_parameter ()
{
echo "$QUERY_STRING" | tr '&' '\n' | grep "^$1=" | head -1 | sed "s/.*=//"
}

       
# Intestazione MIME:
        
echo "Content-Type: text/html"
setcookie tuocodice %ab#67 600
setcookie tuonome   "Mario" 600
setcookie tuocogn   "Rossi" 600
echo

# Corpo del messaggio:
echo "Cookie ritornato dal browser: $HTTP_COOKIE" | ./urldecode
