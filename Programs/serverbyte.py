#!/usr/bin/python          
import socket
import sys
             
out=""
def generate_IR(filename):
	out=""
	ins = open( filename, "r" )
	array = []
	for line in ins:
		    array.append( line )
	ins.close()	
	for i in array:
		i=i.rstrip()
		temp=i.split(':');
		name=temp[0]
		numcourses=len(temp)-1
		marks=[]
		courses=[]
		for x in range(1,len(temp) ):
			intermediate=temp[x].split(',')
			courses.append(intermediate[0])
			marks.append(intermediate[1])
		#print marks
		#print courses
		out+=chr(numcourses)
		out+=chr(len(name))
		out+=name
		for j in range(0,len(courses)):
			out+=chr(len(courses[j]))
			out+=courses[j]
		marksbin=""
		for j in range(0,len(marks)):
			marksbin+=str( bin(int(marks[j]))[2:].zfill(7))
		j=0
		#print len(marksbin)
		while(len(marksbin)%8!=0):
			marksbin+='0'
		while(j<len(marksbin)):
			tempbin=marksbin[j:j+8]
			out+= chr(int(tempbin,2))
			j+=8

	return out
		




intermediate_IR=generate_IR(sys.argv[1])
#print intermediate_IR
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = int(sys.argv[2])           # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
	c, addr = s.accept()     
	print 'Got connection from', addr
	for i in range(0,len(intermediate_IR)):
		c.send(intermediate_IR[i])
	c.close()                
