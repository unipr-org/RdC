
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
parser.add_option('-n', '--name', dest = "name", default = "Balzani")
options, remainder = parser.parse_args()

def sigIntHandler(signum, frame):
    print ("Closing connections...")
    thr = Thread(target = connectionCloser, args = (listaConn, ))
    sys.exit()

sock = socket(AF_INET, SOCK_STREAM)

signal.signal(signal.SIGINT, sigIntHandler)

try:
    sock.connect((options.server, options.port))
except:
    print ("Connection refused!")
    sys.exit(1)

tosend = "GET " + options.uri + " HTTP/1.0\r\n" 
tosend = tosend + "User-Agent: http-client-" + options.name  + "\r\n\r\n"
print (tosend)
sock.send(tosend.encode())

response=""
while True:
  chunk = sock.recv(options.bufsize).decode()
  if chunk == '': 
    break
  response = response + chunk
  
print (response)

sock.close()

