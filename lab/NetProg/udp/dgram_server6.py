#!/usr/bin/env python

# Saverio Mattia Merenda 08/11/2023

import sys, signal, os
#import select
import optparse
from socket import *

parser = optparse.OptionParser()
parser.add_option('-p', '--port',     dest="port", default=9000,  type=int , help="server port" )
parser.add_option('-s', '--server',   dest="server", default="",  help="server IP or name" )
parser.add_option('-6',   action="store_true", dest="ip6", default="False",  help="IPv6" )
parser.add_option('-b', '--bufsize',  dest="bufsize", default=1024,  type=int , help="dimensione buffer" )
options, remainder = parser.parse_args()

print ("   port:", options.port, "  server:", options.server, "bufsize:",options.bufsize, "IPv6:", options.ip6)



if options.ip6 is True:  s = socket(AF_INET6,SOCK_DGRAM)
else:                    s = socket(AF_INET,SOCK_DGRAM)

s.bind((options.server,options.port))

while(1):
        data,addr = s.recvfrom(options.bufsize)
        print ("addr:",addr," data:", data.decode())

