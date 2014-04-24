#!/usr/bin/python          
import socket
import sys
             
out=""
def generate_IR(filename):
	ins = open(filename, "r" )
	array = []
	for line in ins:
		    array.append( line )
	ins.close()
	out="<?xml version=\"1.0\"?><student-record>"


	for i in array:
		#print i
		i=i.rstrip()
		temp=i.split(':');
		out=out+"<student><name>"+temp[0]+"</name>"
		for x in range(1,len(temp) ):
			intermediate=temp[x].split(',')
			out=out+"<course name=\""+intermediate[0]+"\" marks=\""+intermediate[1]+"\"/>"

		out=out+"</student>"
		#print temp
	out=out+"</student-record>"
	return out
		




intermediate_IR=generate_IR(sys.argv[1])
#print intermediate_IR
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = int(sys.argv[2])            # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
	c, addr = s.accept()     
	print 'Got connection from', addr
	for i in range(0,len(intermediate_IR)):
		c.send(intermediate_IR[i])
	c.close()                
