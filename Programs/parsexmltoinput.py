#!/usr/bin/python          
import xml.etree.ElementTree as ET
tree = ET.parse('xml-IR')
root = tree.getroot()
arr=""

for i in range(0,len(root)):
	#print root[i][0].text
	arr=arr+root[i][0].text
	for cr in root[i].iter('course'):
		arr+=":"+cr.attrib['name']+","+cr.attrib['marks']
	if(i!=len(root)-1):
		arr+="\n"
print arr

