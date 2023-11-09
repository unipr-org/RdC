# Saverio Mattia Merenda 08/11/2023

import socket
import sys

if len(sys.argv) < 2:
    name = "www.python.org"
else:
   [name] = sys.argv[1:]

try:
    host = socket.gethostbyname(name)
    print (host)
except socket.gaierror as err:
    print ("cannot resolve hostname: ", name, err)

