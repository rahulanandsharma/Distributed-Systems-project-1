#!/usr/bin/python           
import sys
import socket               # Import socket module
import math
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = int(sys.argv[1])             # Reserve a port for your service.

s.connect((host, port))
out=""
while(1):
	zz=s.recv(1)
	if not zz:
		break
	else:
		out+=zz
f = open('xml-IR','w')
out+="\n"
f.write(out) # python will convert \n to os.linesep
f.close() #




s.close                     # Close the socket when done
