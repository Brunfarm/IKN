import sys
from socket import *


HOST = '10.0.0.1' 	#servers IP-adresse
BUFSIZE = 1000 		#Buffer-størrelse
UPTIME = "/proc/uptime"	
LOADAVG = "/proc/loadavg"
def main(argv):
	#Initialiserer socket
	sock = socket(AF_INET, SOCK_DGRAM)
	sock.bind((HOST, PORT))
	print("Server er klar")
	
	#Programløkke
	while True:
		#Modtager data fra socket
		msg, addr = sock.recvfrom(BUFSIZE)
		
		print("Kommando modtaget: %s" % msg)
		
		#Sender værdi fra uptime
		if msg == "u" or msg == "U":
			file = open(UPTIME)
			data = file.read(BUFSIZE)
			bytesSendt = sock.sendto(data, addr)
			print("%s bytes returneret til %s" % (bytesSendt, addr))
		
		#Eller sender værdi fra loadavg
		elif msg == "l" or msg == "L":
			file = open(LOADAVG)
			data = file.read(BUFSIZE)
			bytesSendt = sock.sendto(data, addr)
			print("%s bytes returneret til %s" % (bytesSendt, addr))
			
		else:
			print("Invalid command")
	

if __name__ == "__main__":
   main(sys.argv[1:])
