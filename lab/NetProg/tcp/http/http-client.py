# Andrea Chiastra, Silvia Balzani, Andia Cecja
# 8 Gennaio 2015

import sys, signal, os
import select
import optparse
from socket import *

parser = optparse.OptionParser()
parser.add_option('-p', '--port', dest = "port", default = 80,  type = int)
parser.add_option('-b', '--bufsize',  dest = "bufsize", default = 2024,  type = int , help="dimensione buffer")
parser.add_option('-s', '--server', dest = "server", default = "localhost")
parser.add_option('-u', '--uri', dest = "uri", default = "/index.html")
parser.add_option('-n', '--name', dest = "name", default = "Cognome")
options, remainder = parser.parse_args()


addr = (options.server,options.port)
sock = socket(AF_INET, SOCK_STREAM)

sock.connect((options.server, options.port))


tosend = "GET " + options.uri + " HTTP/1.0\r\n" 
tosend = tosend + "User-Agent: http-client-" + options.name  + "\r\n\r\n"
print (tosend)
sock.send(tosend.encode())

response=sock.recv(options.bufsize).decode()
print (response)

sock.close()
