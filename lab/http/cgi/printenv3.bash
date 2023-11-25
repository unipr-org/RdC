#!/bin/bash
cat << EOF
Content-Type: text/html

Inserire il mome di una variabile di ambiente:
<form  action="http://${SERVER_NAME}${SCRIPT_NAME}" method="GET" />
<input type="text"  NAME="param" SIZE="15" MAXLENGTH="15" />
<input type="submit" VALUE="    Ok    ">
</form>
<hr>
<pre>
EOF

param=$(echo $QUERY_STRING | sed s/param=//)
echo -n "$param " 
printenv $param | sort
