# Saverio Mattia Merenda 08/11/2023

from threading import Thread
from socket import *
import sys
import optparse


def ascolto(s,addr):
        print ("connessione dal client  ", addr, file = sys.stderr)
        # Receive the data in small chunks and retransmit it
        while True:
                data = s.recv(1500).decode()
                print ("messaggio ricevuto ", data, file = sys.stderr)
                if data:
                      answer=data
                      s.send(answer.encode())
                      print ("messaggio inviato  ", data, file = sys.stderr)
                else:
                      print ("chiusa connessione da ", addr , file = sys.stderr)
                      break


if __name__ == "__main__":

        parser = optparse.OptionParser()
        parser.add_option('-s', '--server',  dest="server",  default="172.17.0.3", help="nome del server" )
        parser.add_option('-p', '--port',    dest="port",    type=int,  default=9056, help="porta di ascolto del server" )
        options, remainder = parser.parse_args()
        print ("OPTIONS  server:", options.server, " - port:", options.port)

        addr = (options.server,options.port)
        sock = socket(AF_INET,SOCK_STREAM)
        # Bind the socket to the port
        print ('server bind sulla porta ',addr, file = sys.stderr)
        sock.bind(addr)
        print ('in attesa di una connessione', file = sys.stderr)
        sock.listen(1)
        while(1):
                connection, client_address = sock.accept()
                #set the thread for the receive request
                ric = Thread(target = ascolto, args = (connection, client_address))
                ric.start()
        sock.close()
