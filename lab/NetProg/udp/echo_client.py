#!/usr/bin/env python

# Saverio Mattia Merenda 08/11/2023

from socket import *
import sys, time
import optparse


parser = optparse.OptionParser()
parser.add_option('-s', '--server',  dest="server",  default="172.17.0.3", help="nome del server" )
parser.add_option('-p', '--port',    dest="port",    type=int,  default=9056, help="porta di ascolto del server" )
parser.add_option('-m', '--message', dest="message", default="hello from Mattia Merenda, in python", help="messaggio  da spedire" )
options, remainder = parser.parse_args()
print ("OPTIONS  server:", options.server, " - port:", options.port, " - message:", options.message)

addr = (options.server,options.port)

s = socket(AF_INET,SOCK_DGRAM)

Len = s.sendto(options.message.encode(),addr)
print ("to: ",addr,"  - data: ",options.message)

data,addr = s.recvfrom(1500)
print ("from:",addr,"- data:", data.decode())

s.close()

