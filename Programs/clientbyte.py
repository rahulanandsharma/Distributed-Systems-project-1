#!/usr/bin/python          
import sys
import socket               # Import socket module
import math
def clienttointermediate(outer):
	out=[]
	for byte in outer:
		out.append(ord(byte))
		
	answer=""
#	print out
	numc=out[0];
	namelen=out[1]
	i=2
	while(i<len(out)):

		uname=out[i:i+namelen]
		i=i+namelen
		answer+=''.join(map(chr,uname))
		#print i 
		courselist=[]
		for j in range(0,numc):
			if(i >= len(out)):
				break;
			cslen=out[i]
			csname=out[i+1:i+cslen+1]
			courselist.append(''.join(map(chr,csname)))
		#answer+=''.join(map(chr,csname))+ ","
		#print i,cslen,csname
			i=i+cslen+1

		numbits=int(math.ceil(7.0*numc/8.0))
		#print numbits
	#print i
		if(i>=len(out)):
			break;
		marksarray=""
		for k in range(0,numbits):
			marks=out[i]
			i+=1
		#print marks
			marksarray+=(str(bin(marks))[2:].zfill(8))
		m=0;
		markslist=[]
		for k in range(0,numc):
			mar=marksarray[m:m+7]
			m=m+7
			markslist.append(int(mar,2))
			#print int(mar,2)

		#print markslist
		#print courselist
		for k in range(0,len(courselist)):
			answer+=":"+courselist[k]+","+str(markslist[k])
		
		if(i >=len(out)):
				break;
		numc=out[i]
		if(i+1>=len(out)):
			break;
		namelen=out[i+1]
		i=i+2
	return answer[:-1]

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = int(sys.argv[1])            # Reserve a port for your service.

s.connect((host, port))
out=""
while(1):
	zz=s.recv(1)
	if not zz:
		break
	else:
		out+=zz
f = open('byte-IR','wb')
f.write(out) # python will convert \n to os.linesep
f.close() #




s.close                     # Close the socket when done
