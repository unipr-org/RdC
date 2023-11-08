#!/usr/bin/env python

# Nome Cognome
# data 
# summary

from socket import *
import sys
import optparse


parser = optparse.OptionParser()
parser.add_option('-s', '--server',   dest="server",  default="", help="nome del server (default localhost)" )
parser.add_option('-p', '--port',     dest="port",    default=9000, type=int, help="porta di ascolto del server" )
parser.add_option('-m', '--message',   dest="message",  default="hello", help="messaggio da inviare" )
parser.add_option('-b', '--bufsize',  dest="bufsize", default=100,  type=int, help="dimensione buffer di spedizione" )
options, remainder = parser.parse_args()
print ("OPTIONS  server:", options.server, " - port:", options.port, " - bufsize:", options.bufsize)

addr = (options.server,options.port)
s = socket(AF_INET,SOCK_DGRAM)

Len=s.sendto(options.message.encode(),addr) 

print ("sent ",Len," Bytes \n")

s.close()

