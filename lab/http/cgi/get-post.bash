#!/bin/bash
#
# Programma get-post.cgi
#

function setcookie()
# $1=NOME $2=CONTENUTO $3=DURATA_IN_SECONDI $4=PERCORSO(OPZ) 
{
value=$( echo -n "$2" | ./urlencode )
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
echo "$qs" | tr '&' '\n' | grep "^$1=" | head -1 | sed "s/.*=//" 
}

############################  ANALIZZA LA RICHIESTA

if [ $REQUEST_METHOD = POST ]
then
QUERY_STRING=`cat`
fi

#qs=$QUERY_STRING
qs=$( echo -n "$QUERY_STRING" | ./urldecode )
Query=$(get_parameter Query)

#####################  INIZIO RISPOSTA 

echo Content-type: text/html
setcookie Method $REQUEST_METHOD 300
setcookie Query $Query 300

echo

echo ""
cat << EOF
<html>
<head>
<title>get-post</title>
</head>
<body bgcolor="steelblue">
<center>
EOF

echo "<strong>http://${SERVER_NAME}:${SERVER_PORT}${SCRIPT_NAME}"
echo "<FORM ACTION=\"http://${SERVER_NAME}:${SERVER_PORT}${SCRIPT_NAME} \" METHOD=GET> "

cat << EOF
GET Query:
<INPUT TYPE="text"  NAME="Query"   MAXLENGTH=100>
<INPUT TYPE="submit" VALUE="Invia">
</FORM>
<p>
EOF

echo "<FORM ACTION=\"http://${SERVER_NAME}:${SERVER_PORT}${SCRIPT_NAME} \" METHOD=POST> "

cat <<EOF
POST Query:
<INPUT TYPE="text"  NAME="Query"   MAXLENGTH=100>
<INPUT TYPE="submit" VALUE="Invia">
</FORM>

</strong>
</center>
<table bgcolor=#ffffff width="80%" height="15%"><tr><td>
EOF

echo "<pre>"
echo
echo $Query

echo "</pre>"
echo "</body>"
echo "</html>"

