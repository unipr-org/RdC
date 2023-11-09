# Saverio Mattia Merenda 08/11/2023

import socket
import sys

if len(sys.argv) < 2:
    addr = "8.8.8.8"
else:
   [addr] = sys.argv[1:]

try:
    print ("gethostbyaddr ",  addr)
    host = socket.gethostbyaddr(addr)
    print (host)
except socket.herror as err:
    print ("cannot resolve name: ", addr, err)

