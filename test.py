'''
-		Operands	Count = 78	System.Collections.Generic.List<string>
		[0]	"import"	string
		[1]	"hashlib"	string
		[2]	"def"	string
		[3]	"hash_file"	string
		[4]	"("	string
		[5]	"filename"	string
		[6]	")"	string
		[7]	":"	string
		[8]	"\"\"\"\"This function returns the SHA-1 hash\n   of the file passed into it\"\"\""	string
		[9]	"h"	string
		[10]	"hashlib"	string
		[11]	"."	string
		[12]	"sha1"	string
		[13]	"("	string
		[14]	")"	string
		[15]	"open"	string
		[16]	"("	string
		[17]	"filename"	string
		[18]	","	string
		[19]	"'rb'"	string
		[20]	")"	string
		[21]	"as"	string
		[22]	"file"	string
		[23]	":"	string
		[24]	"chunk"	string

-		Operators	Count = 11	System.Collections.Generic.List<string>
		[0]	"="	string
		[1]	"with"	string
		[2]	"="	string
		[3]	"while"	string
		[4]	"!="	string
		[5]	"="	string
		[6]	"="	string
		[7]	"="	string
		[8]	"lambda"	string
		[9]	"+"	string
		[10]	"+"	string 
'''
# Python rogram to find the SHA-1 message digest of a file

# importing the hashlib module
import hashlib

def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

message = hash_file("track1.mp3")
print(message)

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))