import sys
from socket import *
from lib import Lib

PORT = 9000
BUFSIZE = 1000
SERVER = '10.0.0.1'

def main(argv):
	sock = socket(AF_INET, SOCK_DGRAM)
	if len(argv) > 0:
		cmd = argv[0]
	else:
		print("Brug 'file_client.py(<filnavn>)")
		sys.exit()
	sock.connect((SERVER,PORT))
	print("Forbundet til server")
	Lib.writeTextTCP(cmd,sock)

	fileSize = Lib.getFileSizeTCP(sock)
	
	
	if fileSize > 0:
		recieveFile(cmd, sock)
	else:
		print("Fil ikke fundet")
		sys.exit()
	sock.close()
		
    
def receiveFile(cmd,  conn):
	bytesRead = 0
	fileName = Lib.extractFilename(cmd)
	file = open(fileName, 'wb')

	while bytesRead < fileSize:
		buff = conn.recv(BUFSIZE)
		file.write(buff)
		bytesRead = bytesRead+len(buff)
	print("Transfer complete")

if __name__ == "__main__":
   main(sys.argv[1:])
