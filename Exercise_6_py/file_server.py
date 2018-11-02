import sys
from socket import *
from lib import Lib

HOST = '10.0.0.1'
PORT = 9000
BUFSIZE = 1000
def main(argv):
	servSock = socket(AF_INET, SOCK_STREAM)
	servSock.bind((HOST, PORT))
	servSock.listen(1)
	print("The server is ready to recieve")
	while True:
		conSock, addr = servSock.accept()
		print("client connected")
		msg = Lib.readTextTCP(conSock)
		while msg != "exit":
			print("Command received: %s" % msg)
		
			fileSize = Lib.check_File_Exists(msg)
	
			if fileSize > 0:
				
				sendFile(msg, fileSize, conSock)
			else:
				Lib.writeTextTCP(str(fileSize), conSock)
			msg = Lib.readTextTCP(conSock)
		conSock.close()
	
	

def sendFile(fileName,  fileSize,  conn):
	Lib.writeTextTCP(str(fileSize), conn)
	file = open(fileName, 'rb')
	data = file.read(BUFSIZE)
	while data:
		conn.send(data)
		data = file.read(BUFSIZE)
    
if __name__ == "__main__":
   main(sys.argv[1:])
