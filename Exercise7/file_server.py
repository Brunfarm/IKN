import sys
from socket import *


HOST = '10.0.0.1' 	
BUFSIZE = 1000 		
UPTIME = "/proc/uptime"	
LOADAVG = "/proc/loadavg"
PORT = 9000
def main(argv):

	sock = socket(AF_INET, SOCK_DGRAM)
	sock.bind((HOST, PORT))
	print("Server er klar")
	
	
	while True:
		
		msg, addr = sock.recvfrom(BUFSIZE)
		
		print("Kommando modtaget: %s" % msg)
		
		
		if msg == "u" or msg == "U":
			file = open(UPTIME)
			data = file.read(BUFSIZE)
			bytesSendt = sock.sendto(data, addr)
			print("%s bytes returneret til %s" % (bytesSendt, addr))
		
		
		elif msg == "l" or msg == "L":
			file = open(LOADAVG)
			data = file.read(BUFSIZE)
			bytesSendt = sock.sendto(data, addr)
			print("%s bytes returneret til %s" % (bytesSendt, addr))
			
		else:
			print("Invalid command")
	

if __name__ == "__main__":
   main(sys.argv[1:])
