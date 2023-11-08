#!/usr/bin/env python

# Nome Cognome, data
# Summary :

from socket import *
import sys, time
import optparse


parser = optparse.OptionParser()
parser.add_option('-s', '--server',  dest="server",  default="localhost", help="nome del server" )
parser.add_option('-p', '--port',    dest="port",    type=int,  default=9000, help="porta di ascolto del server" )
parser.add_option('-m', '--message', dest="message", default="hello from Cognome, in python", help="messaggio  da spedire")
options, remainder = parser.parse_args()
print ("OPTIONS  server:", options.server, " - port:", options.port, " - message:", options.message)

addr = (options.server,options.port)
s = socket(AF_INET,SOCK_STREAM)

s.connect(addr)
print ("Connesso al server", addr)
messaggio="ciao"
print ("Invio messaggio ", messaggio)
s.send(messaggio.encode())
risposta = s.recv(1500).decode()
#print (type(risposta))
print ("Risposta del server: " , risposta)
s.close()

