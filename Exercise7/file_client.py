import sys
from socket import *

PORT = 9000
BUFSIZE = 1000
SERVER = '10.0.0.1'

def main(argv):
	
	sock = socket(AF_INET, SOCK_DGRAM)
		
	while True:
		
		msg = input("Indtast 'U' for uptime, eller 'L' for loadavg\n")
		
		if msg == "U" or msg == "u":		
			sock.sendto(msg, (SERVER, PORT))
			
			data, addr = sock.recvfrom(BUFSIZE)
			
			print("Serverens uptime er: %s" % data)
		elif msg == "L" or msg == "l":		
			sock.sendto(msg, (SERVER, PORT))
			
			data, addr = sock.recvfrom(BUFSIZE)
			#
			print("Serverens CPU load er: %s" % data)
		else:
			print("Ugyldig kommando")
if __name__ == "__main__":
   main(sys.argv[1:])
