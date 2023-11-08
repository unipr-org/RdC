
# Saverio Mattia Merenda 08/11/2023

from threading import Thread
from socket import *
import sys
import optparse



def ascolto(s,addr):
        print ("connessione dal client  ", addr, file = sys.stderr)
        data = s.recv(1500).decode()
        print ('ricevuto ',data, file = sys.stderr)
        answer=data
        s.send(answer.encode())
        print ('inviato ' , answer, file = sys.stderr)



if __name__ == "__main__":
        parser = optparse.OptionParser()
        parser.add_option('-s', '--server',  dest="server",  default="172.17.0.3", help="nome del server" )
        parser.add_option('-p', '--port',    dest="port",    type=int,  default=9056, help="porta di ascolto del server" )
        options, remainder = parser.parse_args()
        print ("OPTIONS  server:", options.server, " - port:", options.port)

        addr = (options.server,options.port)
        sock = socket(AF_INET,SOCK_STREAM)

        print ('starting up on port ',addr, file = sys.stderr)
        sock.bind(addr)

        # Listen for incoming connections
        sock.listen(1)
        print ('in attesa di una connessione', file = sys.stderr)

        # Wait for a connection
        while(1):
                s2, c_addr = sock.accept()
                #set the thread for the receive request
                ric = Thread(target = ascolto, args = (s2,c_addr))
                ric.start()
        sock.close()
