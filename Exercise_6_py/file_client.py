import sys
from socket import *
from lib import Lib

PORT = 9000
BUFSIZE = 1000
SERVER = '10.0.0.1'

def main(argv):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.connect((SERVER,PORT))
	print("Forbundet til server")
	cmd = input("Indtast filnavn. Ved afslutning skriv 'exit'\n")
	while cmd != "exit":
		Lib.writeTextTCP(cmd,sock)

		fileSize = Lib.getFileSizeTCP(sock)
		print(fileSize)
	
		if fileSize > 0:
			receiveFile(cmd, sock, fileSize)
		else:
			print("Fil ikke fundet")
		cmd = input("Indtast filnavn. Ved afslutning skriv 'exit'\n")
	sock.close()
	sys.exit()
		
    
def receiveFile(nm,  conn, siz):
	bytesRead = 0
	fileName = Lib.extractFilename(nm)
	file = open(fileName, 'wb')

	while bytesRead < siz:
		buff = conn.recv(BUFSIZE)
		file.write(buff)
		bytesRead = bytesRead+len(buff)
	print("Transfer complete")

if __name__ == "__main__":
   main(sys.argv[1:])
