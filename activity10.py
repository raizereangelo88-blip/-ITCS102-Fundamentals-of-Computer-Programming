from getpass import getpass
username = 'raizrz'
password = 'rainotgood'
 
u = input("USERNAME --> ")
p = getpass("PASSWORD --> ")

if (u == username) and (p == password) :
	print("Access Granted")	 	 	 	
else: 		 	 	
	print("Access Denied")	 	 	 	    	