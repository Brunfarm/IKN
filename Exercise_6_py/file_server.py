import sys
from socket import *
from lib import Lib

LOCALIP = '0.0.0.0' 
PORT = int(sys.argv[1])
BUFSIZE = 1000
def main(argv):

	
	serverSocket = socket(AF_INET, SOCK_STREAM)
	serverSocket.bind((LOCALIP, PORT))
	serverSocket.listen(1) 
	print("The server is ready to recieve\n")
	while True:
		connectionSocket, addr = serverSocket.accept()
		print("client connected\n")
		msg = Lib.readTextTCP(connectionSocket)
		while msg != "exit":
			print("Command received: %s\n" % msg)
			fileSize = Lib.check_File_Exists(msg)
	
			if fileSize > 0:
				
				sendFile(msg, fileSize, connectionSocket)
			else:
				Lib.writeTextTCP(str(fileSize), connectionSocket)
			msg = Lib.readTextTCP(connectionSocket)
		connectionSocket.close()
		print("Connection closed")
	
	

def sendFile(fileName,  fileSize,  conn):
	Lib.writeTextTCP(str(fileSize), conn)
	file = open(fileName, 'rb')
	data = file.read(BUFSIZE)
	while data:
		conn.send(data)
		data = file.read(BUFSIZE)
    
if __name__ == "__main__":
   main(sys.argv[1:])
