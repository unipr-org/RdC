# Silvia Balzani, Andrea Chiastra, Andia Cecja
# 8 Gennaio 2015

from threading import Thread
import sys, signal, os
import select
import optparse
from socket import *

listaConn = []

parser = optparse.OptionParser()
parser.add_option('-p', '--port', dest = "port", default = 25001,  type = int)
parser.add_option('-b', '--bufsize',  dest = "bufsize", default = 1024,  type = int , help="dimensione buffer")
parser.add_option('-n', '--name',  dest = "name", default = "Silvia Balzani",  help="nome")
options, remainder = parser.parse_args()

def comunicationHandler(connection, addr):
    mex = connection.recv(options.bufsize).decode()
    print ("Address ", addr, " sent the following message: ", mex)
    while(mex[0] == ' '):
        mex = mex[1:-1]
    if (mex[0:3] == 'GET'):
        mexb = "HTTP/1.0 200 OK\r\nHost: didattica-linux\r\nServer: " + options.name + "\r\nContent-Type: text/html\r\nContent-Length: 254\r\n\r\n"
        mexb = mexb + "<html>\r\n<head>\r\n<title> TITOLO </title>\r\n</head>\r\n"
        mexb = mexb + "<body>\r\n<b> Risposta dal server HTTP in ascolto sulla porta " + str(options.port) + "</b> <p>\r\n</body>\r\n</html>\r\n"
        print("The length of the answer  is ", str(len(mexb)))
        print ("Sending html page")
        connection.send(mexb.encode())
    print ("Communication with ", addr, " has ended")
    connection.close()

def connectionCloser(lista):
    for co in lista:
        try:
                co.close()
        except:
                pass

sockConn = socket(AF_INET, SOCK_STREAM)

def sigIntHandler(signum, frame):
    print ("Closing connections...")
    sockConn.close()
    thr = Thread(target = connectionCloser, args = (listaConn, ))
    sys.exit()


sockConn.bind(('0.0.0.0', options.port))
sockConn.listen(1)

signal.signal(signal.SIGINT, sigIntHandler)

while(True):
    print ("Waiting for connections on port", options.port)
    connection, addr = sockConn.accept()
    listaConn = listaConn + [connection]
    thr = Thread(target = comunicationHandler, args = (connection, addr, ))
    thr.setDaemon(True)
    print ("Started comunication with ", addr)
    thr.start()

