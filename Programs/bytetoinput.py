#!/usr/bin/python          
import math
import sys
f = open("byte-IR", "rb")
def converttorecord(mylist):
	print mylist 
out=[]
try:
        byte = f.read(1)
	i=0;
        while byte != "":
		#print ord(byte),
		out.append(ord(byte))
		byte = f.read(1)

	
		#print byte,ord(byte)
finally:
	answer=""
        f.close()
#	print out
	
	numc=out[0];
	if(len(out)<=1):
		sys.exit()
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
		answer+="\n"
		if(i >=len(out)):
				break;
		numc=out[i]
		if(i+1>=len(out)):
			break;
		namelen=out[i+1]
		i=i+2
	print answer[:-1]


		
	
