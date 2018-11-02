import sys
from socket import *


HOST = '10.0.0.1'
PORT = 9000
BUFSIZE = 1000
UPTIME = "/proc/uptime"
LOADAVG = "/proc/loadavg"
def main(argv):
	sock = socket(AF_INET, SOCK_DGRAM)
	servSock.bind((HOST, PORT))
	
	while True:
		msg, addr = sock.recvfrom(BUFSIZE)
		
		print(msg)
	
		if msg == "u" or msg == "U":
			file = open(UPTIME)
			data = file.read(BUFSIZE)
			sock.sendto(data, addr)
		elif data == "l" or data == "L":
			file = open(LOADAVG)
			data = file.read(BUFSIZE)
			sock.sendto(data, addr)
			
		else:
			print("Invalid command")
	

if __name__ == "__main__":
   main(sys.argv[1:])
