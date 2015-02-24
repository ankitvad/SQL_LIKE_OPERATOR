query = raw_input("enter the search string:")
all_names = open("first_names.txt",'rb')
names = all_names.read().split('\r\n')
all_names.close()
for i in range(0,len(names)):
	if(names[i] == query):
		print(query+" Found")
