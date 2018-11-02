import sys
from socket import *

PORT = 9000
BUFSIZE = 1000
SERVER = '10.0.0.1'

def main(argv):
	sock = socket(AF_INET, SOCK_DGRAM)
	while True:
		msg = input("Indtast 'U' for uptime, eller 'L' for loadavg")
		
		sock.sendto(msg, (SERVER, PORT))
		data, addr = sock.recvfrom(BUFSIZE)
		print(data)


if __name__ == "__main__":
   main(sys.argv[1:])
