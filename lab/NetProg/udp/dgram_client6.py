#!/usr/bin/env python

# Saverio Mattia Merenda 08/11/2023

from socket import *
import sys, time
import optparse


parser = optparse.OptionParser()
parser.add_option('-s', '--server',   dest="server",  default="", help="nome del server" )
parser.add_option('-p', '--port',     dest="port",    default=9000, type=int, help="porta di ascolto del server" )
parser.add_option('-b', '--bufsize',  dest="bufsize", default=100,  type=int, help="dimensione buffer di spedizione" )
parser.add_option('-m', '--message',   dest="message",  default="hello IP6", help="messaggio da inviare" )

parser.add_option('-6',   action="store_true", dest="ip6", default="False",  help="IPv6" )

options, remainder = parser.parse_args()
print ("OPTIONS  server:", options.server, " - port:", options.port, " - bufsize:", options.bufsize)

addr = (options.server,options.port)

if options.ip6 is True:  s = socket(AF_INET6,SOCK_DGRAM)
else:                    s = socket(AF_INET,SOCK_DGRAM)


Len = s.sendto(options.message.encode(),addr)
print ("sent ",Len," Bytes \n")


s.close()
