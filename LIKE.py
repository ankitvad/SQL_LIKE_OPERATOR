import re
query = raw_input("enter the search string:")
x = []
x.append("^")
#Converting Query to REGEX.
for i in range(0,len(query)):
	if(query[i] == "_"):
		x.append("[a-zA-Z0-9\-\.\_\'\"]")
	elif(query[i]== "%"):
		x.append("[a-zA-Z0-9\-\.\_\'\"]*")
	else:
		x.append(query[i])

x.append("[^a-zA-Z0-9\-\.\_\'\"]")
x = ''.join(x)

#print x
#print(x)

all_names = open("first_names.txt",'r')
name = all_names.readline()
while name:
	if(re.search(x,name)):
		#THIS FOR CASE INSENSITIVITY..
	#if(re.search(x.lower(),name.lower())):
		print(name+"\t")
	name = all_names.readline()
all_names.close()

