#!/bin/bash
echo "Content-Type: text/html"
echo
echo " <a href=http://${SERVER_NAME}${REQUEST_URI}> printenv | sort</a>"
echo "<pre>"
printenv | sort
echo "</pre>"

