Assignment1
===========
For each of the formats (XML and Byte Representation) there are two programs say a server and a client. The server is given the input file in the form of rows as specified earlier. It converts the input to the appropriate intermediate representation and sends it as a byte stream to the client. The client then converts back the intermediate representation to the original format and outputs it. So, 4 programs in total.


Byte Representation


Example-1: Now, let us say there are three marks in total. So, a total of 3*7 = 21 bits. But, it is not a multiple of 8. So, we append 3 0's to get 24 bits and then send it byte by byte.


Example-2: If the number of marks are 8, we get a total of 8*7 = 56 bits which is already a multiple of 8. So we get a total of 56/8 = 7 bytes and then send them.


I have also attached sample files for you to go through.


"byte-IR" and "xml-IR" are the intermediate representations that u get. 


"byte-Output" and "xml-Output" are the files that you get when you unmarshall the data in the client programs. They are supposed to be same.
