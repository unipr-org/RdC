#!/usr/bin/env python3

# Saverio Mattia Merenda 08/11/2023

from socket import *
import sys, time
import optparse
import signal, os

parser = optparse.OptionParser()
parser.add_option('-s', '--server',  dest="server",  default="localhost", help="nome del server")
parser.add_option('-p', '--port',    dest="port",    type=int,  default=9000, help="porta di ascolto del server")
parser.add_option('-t', '--timeout',    dest="timeout",    type=int,  default=5, help="timeout per aspettare risposta")
parser.add_option('-m', '--message', dest="message", default="hello from ... , in python", help="messaggio  da spedire in risposta")
options, remainder = parser.parse_args()
# print ("OPTIONS  server:", options.server, " - port:", options.port, " - message:", options.message, " - timeout:", options.timeout)

def handler_alrm(signum, frame):
    print('Timeout. No reply')
    sys.exit(0)


# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler_alrm)

addr = (options.server,options.port)
s = socket(AF_INET,SOCK_DGRAM)

Len = s.sendto(options.message.encode(),addr)
print ("Message to: ", addr, " - data: ", options.message)

signal.alarm(options.timeout)
data,addr = s.recvfrom(1500)

print ("Message from:", addr, "- data:", data.decode())

s.close()
